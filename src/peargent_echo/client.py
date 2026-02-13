import requests
from typing import Optional, Dict, Any, List, Union

class PeargentEcho:
    def __init__(self, api_key: str, base_url: str = "https://echo.peargent.online/api/v1"):
        self.api_key = api_key
        self.base_url = base_url.rstrip('/')

    def _request(self, method: str, path: str, **kwargs) -> Dict[str, Any]:
        url = f"{self.base_url}/{path.lstrip('/')}"
        headers = kwargs.pop("headers", {})
        headers.update({
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        })

        response = requests.request(method, url, headers=headers, **kwargs)
        
        try:
            data = response.json()
        except ValueError:
            response.raise_for_status()
            return {}

        if not response.ok:
            error_msg = data.get("message") or data.get("error") or "Unknown error"
            raise Exception(f"Peargent Echo API Error: {error_msg}")

        return data

    def add_memory(
        self,
        content: str,
        agent_id: Optional[str] = None,
        run_id: Optional[str] = None,
        source: Optional[str] = None,
        metadata: Optional[Dict[str, Any]] = None,
        filter: bool = True,
        extract: bool = True,
        update_profile: bool = True
    ) -> Dict[str, Any]:
        """
        Add a new memory to the user's graph.
        """
        payload = {
            "content": content,
            "filter": filter,
            "extract": extract,
            "updateProfile": update_profile
        }
        
        if agent_id: payload["agentId"] = agent_id
        if run_id: payload["runId"] = run_id
        if source: payload["source"] = source
        if metadata: payload["metadata"] = metadata

        return self._request("POST", "/memories", json=payload)

    def search(
        self,
        query: str,
        limit: int = 10,
        agent_id: Optional[str] = None,
        run_id: Optional[str] = None,
        include_graph: bool = False
    ) -> Dict[str, Any]:
        """
        Search for memories semantically.
        """
        payload = {
            "query": query,
            "limit": limit,
            "includeGraph": include_graph
        }

        if agent_id: payload["agentId"] = agent_id
        if run_id: payload["runId"] = run_id

        return self._request("POST", "/search", json=payload)

    def get_profile(self, query: Optional[str] = None, limit: int = 5) -> Dict[str, Any]:
        """
        Get the user's profile context.
        """
        params = {"limit": limit}
        if query:
            params["q"] = query
            
        return self._request("GET", "/profile", params=params)
