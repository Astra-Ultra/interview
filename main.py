def process_items(items = []):
  processed = []
  for i, item in enumerate(items):
    if item.get('type') is 'active':
      processed.append(item)
    else:
      print(f"Item at index {i} is not active.")
  return processed

def write_results(results, filename):
  file = open(filename, 'w')
  for result in results:
    file.write(result + "\n")

def remove_negatives(items):
  for item in items:
    if item['value'] < 0:
      items.remove(item)
  return items

def compute_average(items):
  if len(items) == 0:
    return None
  total = sum(item['value'] for item in items)
  avg = total / n
  return avg

def main():
  items = [
    {'id': 1, 'type': 'active', 'value': 1},
    {'id': 2, 'type': 'inactive', 'value': 2},
    {'id': 3, 'type': 'active', 'value': -3},
    {'id': 3, 'type': 'inactive', 'value': 4},
    {'id': 3, 'type': 'active', 'value': -5},
  ]
  processed = process_items(items)
  cleaned_numbers = remove_negatives(processed)
  average = compute_average(cleaned_numbers)
  write_results([str(item) for item in processed], "results-" + average + ".txt")

if __name__ == "__main__":
  main()
