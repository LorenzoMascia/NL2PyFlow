// TextEditor.js
function TextEditor({ text, onChange, onGenerate, isLoading }) {
  return (
    <div className="editor-container">
      <textarea
        className="text-editor"
        value={text}
        onChange={(e) => onChange(e.target.value)}
        placeholder={`Write the workflow description here...
        
Example:
### Block 1: Import Data
Loads data from CSV file and prepares the dataframe

### Block 2: Data Cleaning
Preprocesses data and handles missing values

### Block 3: Train Model
Trains the machine learning model on the prepared data`}
      />
      <button 
        className="generate-button" 
        onClick={onGenerate}
        disabled={isLoading}
      >
        {isLoading ? (
          <>
            <i className></i> Generation...
          </>
        ) : (
          <>
            <i className="fas fa-circle-play"></i> Generate Blocks
          </>
        )}
      </button>
    </div>
  );
}