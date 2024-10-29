class Community:
    def __init__(self, name, description, page_name:str=None):
        self.name = name
        self.description = description
        self.page_name = page_name or name.lower().replace(" ", "_").replace("🎨", "").replace("📚", "").replace("🧘‍♀️", "").replace("🍽️", "").replace("🧘‍♂️", "").replace("💰", "").replace("💅", "").replace("🎉", "").replace("👗", "")
