---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S LinkReferenceData"
source_ids: ["src-000366"]
source_editions: ["december-2024"]
message_ids: []
heading_path: ["8 Message Items Types", "8.1 MessageComponents", "8.1.2 Account Identification", "8.1.2.2 AccountIdentification4Choice", "8.1.2.2.1 IBAN <IBAN>"]
file_pages: [60]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 8.1.2.2.1 IBAN <IBAN>

Source: [src-000366](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_LinkReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_LinkReferenceData_v1.pdf`. Locator: one-based file pages 60 to 60.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 60

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   IBAN <IBAN> [1..1] IdentifierSet C2 60
Or}   Other <Othr> [1..1] ± 60
8.1.2.2.1  IBAN <IBAN>
Presence: [1..1]
Definition: International Bank Account Number (IBAN) - identifier used internationally by financial
institutions to uniquely identify the account of a customer. Further specifications of the format and
content of the IBAN can be found in the standard ISO 13616 "Banking and related financial services -
International Bank Account Number (IBAN)" version 1997-10-01, or later revisions.
Impacted by: C2 "IBAN"
Datatype: "IBAN2007Identifier" on page 76
Constraints
• IBAN
A valid IBAN consists of all three of the following components: Country Code, check digits and
BBAN.
8.1.2.2.2  Other <Othr>
Presence: [1..1]
Definition: Unique identification of an account, as assigned by the account servicer, using an
identification scheme.
Other <Othr> contains the following elements (see "GenericAccountIdentification1" on page 58 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 58
   SchemeName <SchmeNm> [0..1]  58
{Or     Code <Cd> [1..1] CodeSet 58
Or}     Proprietary <Prtry> [1..1] Text 58
   Issuer <Issr> [0..1] Text 59
8.1.3 Date Time
8.1.3.1  DateAndDateTime2Choice
Definition: Choice between a date or a date and time format.
Approved by the Securities SEG on 21 November 2024. Message Items Types
Target2-Securities - Link Reference Data 60 December 2024
```

