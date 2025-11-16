"""High-level tests for pkg package."""


def test_package() -> None:
    """Test importing the pkg package."""
    import pkg  # noqa: PLC0415

    assert pkg.__name__ == "pkg"
