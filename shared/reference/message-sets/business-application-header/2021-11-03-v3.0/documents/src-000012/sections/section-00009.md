---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "shared"
message_set: "Business Application Header"
source_ids: ["src-000012"]
source_editions: ["Version 3.0 2021-11-03"]
message_ids: []
heading_path: ["2 Scenarios", "2.3 Business Application A informs Business Application B that Text based MessageElements (in the BAH or the BusinessMessage) may contain non-Basic-Latin characters"]
file_pages: [11]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 2.3 Business Application A informs Business Application B that Text based MessageElements (in the BAH or the BusinessMessage) may contain non-Basic-Latin characters

Source: [src-000012](../../../../../../../../raw-input/business_application_header/ISO_20022_BusinessApplicationHeader_MUG_v3_0.pdf). Locator: one-based file pages 11 to 11.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 11

```text
11 ISO 20022 Business Application Header Message Usage Guide v3.0  
There may be several CreationDate elements but they may not have the same definition. 
As a general rule, the CreationDate in the BusinessApplicationHeader contains the date and time at 
which the Business Message was produced by the BusinessApplication. The term BusinessApplication 
must be interpreted in a broad sense: it may be a payments factory application; it may also be an 
operator at a screen who is manually inputting the business information. 
Depending on the definition that is given to a CreationDate in the ISO 20022 Message (Document 
XML element) itself, the date and time could vary from the date and time in the Business Application 
Header. The creation date in the BAH applies to the entire Business Message whereas other creation 
dates apply to only parts of the Business Message. 
 
EXAMPLE 
1 John Doe at Bank A prepares the payments; 
2 The same person creates an activity report on September 28th at 09:00AM UTC; 
3 The same person signs it at 9:50AM UTC with the signature in the BAH; 
4 The BAH contains the CreationDate of the BusinessMessage, the Document contains the 
CreationDate of the activity report. 
 
 
 
2.3  Business Application A informs Business Application B  
that Text based MessageElements (in the BAH or the 
BusinessMessage) may contain non -Basic-Latin characters  
 
In this case, each additional character set will be specified in the Char acterSet MessageElement, 
separated by a semicolon. 
All relevant Text based Datatypes may then contain characters belong ing to the character sets 
specified in this MessageElement. 
Some Text based DataTypes may be further constrained than what is specified here in which case the 
character set restrictions specified in the BAH do not apply. 
  
<AppHdr> 
 
<CreDt>2009-09-28T09:50:00Z</CreDt> 
 
</AppHdr> 
(3) 
<Document> 
<ActvtyRpt>… 
<RptId> 
<CrDtTm>2009-09-28T09:00:00Z</CrDtTm> 
</RptId> 
</ ActvtyRpt > 
</Document> 
(2) 
```

