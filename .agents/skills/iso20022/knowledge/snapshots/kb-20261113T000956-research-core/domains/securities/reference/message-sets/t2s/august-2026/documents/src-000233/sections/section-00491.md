---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["26 head.002.001.01 BusinessFileHeaderV01", "26.4 Message Building Blocks", "26.4.1 PayloadDescription <PyldDesc>", "26.4.1.2 ApplicationSpecifics <ApplSpcfcs>"]
file_pages: [617]
content_origin: "source-text-extraction"
mentioned_message_ids: ["head.002.001.01"]
---

# 26.4.1.2 ApplicationSpecifics <ApplSpcfcs>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 617 to 617.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 617

```text
Definition: Flag indicating if the file exchanged between the two business applications is possibly a
duplicate. If this indicator is not present within the message, please note that the default value would be
"False".
Datatype: One of the following values must be used (see "TrueFalseIndicator" on page 3323):
• Meaning When True: True
• Meaning When False: False
26.4.1.2  ApplicationSpecifics <ApplSpcfcs>
Presence: [0..1]
Definition: Contains business information that is considered as necessary by the service provider.
ApplicationSpecifics <ApplSpcfcs> contains the following ApplicationSpecifics1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SystemUser <SysUsr> [0..1] Text 617
   Signature <Sgntr> [0..1] (External Schema) 617
   TotalNumberOfDocuments <TtlNbOfDocs> [1..1] Quantity 617
26.4.1.2.1  SystemUser <SysUsr>
Presence: [0..1]
Definition: A system user is a user account defined in the static data. It represents an individual or an
application that interacts with the system administrator (e. g. T2S), triggering the available functions.
The set of functions available to each system user stems from the set of privileges for which the system
user is grantee. System administrator does not provide any attribute for distinguishing between
individuals and applications. 
Datatype: "Max140Text" on page 3326
26.4.1.2.2  Signature <Sgntr>
Presence: [0..1]
Definition: Contains the digital signature of the Business Entity authorised to sign this Business File.
Type: (External Schema)
The W3C XML Schema that specifies following standard signature:
XML Signature Syntax and Processing (Second Edition) W3C Recommendation 10 June 2008
http://www.w3.org/TR/2008/REC-xmldsig-core-20080610/.
26.4.1.2.3  TotalNumberOfDocuments <TtlNbOfDocs>
Presence: [1..1]
Definition: Gives the total number of instances (messages) within the file.
Datatype: "Number" on page 3324
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
head.002.001.01 BusinessFileHeaderV01
Target2-Securities 617 August 2026
```

