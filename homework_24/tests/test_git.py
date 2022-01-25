def test_a(dashboard_page):
    a = dashboard_page.select_overview()
    assert "https://github.com/artbilan" == a.current_url





