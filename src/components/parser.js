import { parse } from 'csv-parse/sync';

class CSVParser {
  constructor(filePath) {
    this.filePath = filePath;
  }

  async parse() {
    try {
      const data = await import('fs').then(fs => fs.readFileSync(this.filePath, 'utf8'));
      const records = parse(data, {
        from: 1,
        columns: true,
        skip_empty_lines: true
      });
      return records;
    } catch (error) {
      throw new Error(`Failed to parse CSV file: ${error.message}`);
    }
  }
}

export default CSVParser;