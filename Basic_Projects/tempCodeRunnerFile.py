 def update_result(self, text: str):
        # Update the result entry with the calculated tax amount
        self.result_entry.delete(0, ctk.END)
        self.result_entry.insert(0, text)