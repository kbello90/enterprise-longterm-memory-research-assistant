def run():
    from app.observability.logging import setup_logging
    from app.api.routes_chat import router as chat_router
    from app.api.routes_memory import router as memory_router
    from app.agent.orchestrator import run_agent
    from app.memory.local_store import load_profile, add_episode, update_preferences

    assert callable(setup_logging)
    assert chat_router is not None
    assert memory_router is not None
    assert callable(run_agent)
    assert callable(load_profile)
    assert callable(add_episode)
    assert callable(update_preferences)

    print("✅ Sanity check passed: core imports and exports are valid.")

if __name__ == "__main__":
    run()
