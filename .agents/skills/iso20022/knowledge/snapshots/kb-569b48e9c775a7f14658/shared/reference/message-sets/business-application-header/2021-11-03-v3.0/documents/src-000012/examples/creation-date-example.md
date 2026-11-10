---
template: false
review_status: "needs-review"
domain: "shared"
document_kind: "source-example"
source_ids: ["src-000012"]
source_edition: "Version 3.0, 2021-11-03"
curated: true
file_pages: [11]
source_locations: ["§2.2 CreationDate example"]
limitations: ["Source example retained; exact executable XML/cryptographic validity is not claimed."]
source_editions: ["Version 3.0 2021-11-03"]
---

# §2.2 CreationDate example

[src-000012](../../../../../../../../evidence/omitted/2bef0f7d99f68f11e72a140f.md), file/printed page 11, §2.2 CreationDate example.

The example names John Doe at Bank A as an operator: prepares payments, produces an activity report at 09:00 UTC, then signs at 09:50 UTC. BAH CreDt is 2009-09-28T09:50:00Z; the document report CrDtTm is 2009-09-28T09:00:00Z. Callouts (3) and (2) distinguish those instants. The narrative broadens BusinessApplication to a payments factory or a person manually entering business data. The source contains example ellipses; they are not unfinished repository placeholders.

[Complete original example rendered from PDF](../../../../../../../../evidence/omitted/92ec2607e671aea75d5d908a.md)

## Preserved source text

This is the verbatim text extraction, including extraction spacing or replacement characters. Use the source page when exact lexical fidelity matters.

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

## Source components

- [fig-0014 original image component](../../../../../../../../evidence/omitted/d9f7ef9a8da24511c3fb012d.md).
- [fig-0015 original image component](../../../../../../../../evidence/omitted/6d683452c3b9464397d85549.md).
- [fig-0016 original image component](../../../../../../../../evidence/omitted/844cd8a7d1c1eba646f1fd0f.md).
- [fig-0017 original image component](../../../../../../../../evidence/omitted/aedc896da3d0ff88379c7791.md).
- [fig-0018 original image component](../../../../../../../../evidence/omitted/7309523bb33e132cf5d20438.md).
- [fig-0019 original image component](../../../../../../../../evidence/omitted/508e267cbbfa91543550f52c.md).
