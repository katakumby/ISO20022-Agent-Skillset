---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["22 Message Items Types", "22.1 MessageComponents", "22.1.5 Financial Instrument", "22.1.5.8 SecurityIdentification19", "22.1.5.8.1 ISIN <ISIN>"]
file_pages: [330]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 22.1.5.8.1 ISIN <ISIN>

Source: [src-000321](../../../../../../../../../evidence/omitted/8d2c320c3a6fbfe4d503c6ab.md). Locator: one-based file pages 330 to 330.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 330

```text
On Condition
    /OtherIdentification[*] is absent
Following Must be True
    /ISIN Must be present
 Or    /Description Must be present
22.1.5.8.1  ISIN <ISIN>
Presence: [0..1]
Definition: International Securities Identification Number (ISIN). A numbering system designed by the
United Nation's International Organisation for Standardisation (ISO). The ISIN is composed of a 2-
character prefix representing the country of issue, followed by the national security number (if one
exists), and a check digit. Each country has a national numbering agency that assigns ISIN numbers for
securities in that country.
Datatype: "ISINOct2015Identifier" on page 450
22.1.5.8.2  OtherIdentification <OthrId>
Presence: [0..*]
Definition: Identification of a security by proprietary or domestic identification scheme.
OtherIdentification <OthrId> contains the following OtherIdentification1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 330
   Suffix <Sfx> [0..1] Text 330
   Type <Tp> [1..1] ± 330
22.1.5.8.2.1  Identification <Id>
Presence: [1..1]
Definition: Identification of a security.
Datatype: "Max35Text" on page 456
22.1.5.8.2.2  Suffix <Sfx>
Presence: [0..1]
Definition: Identifies the suffix of the security identification.
Datatype: "Max16Text" on page 455
22.1.5.8.2.3  Type <Tp>
Presence: [1..1]
Definition: Type of the identification.
Approved by the Securities SEG on 17 July 2025 Message Items Types
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
330 July 2025
```

