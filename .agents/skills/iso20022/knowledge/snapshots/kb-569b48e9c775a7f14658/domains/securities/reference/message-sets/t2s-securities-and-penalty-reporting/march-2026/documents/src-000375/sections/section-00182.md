---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.2 Account Identification", "7.1.2.3 AccountIdentification4Choice", "7.1.2.3.1 IBAN <IBAN>"]
file_pages: [250]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.2.3.1 IBAN <IBAN>

Source: [src-000375](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 250 to 250.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 250

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   IBAN <IBAN> [1..1] IdentifierSet C8 250
Or}   Other <Othr> [1..1] ± 250
7.1.2.3.1  IBAN <IBAN>
Presence: [1..1]
Definition: International Bank Account Number (IBAN) - identifier used internationally by financial
institutions to uniquely identify the account of a customer. Further specifications of the format and
content of the IBAN can be found in the standard ISO 13616 "Banking and related financial services -
International Bank Account Number (IBAN)" version 1997-10-01, or later revisions.
Impacted by: C8 "IBAN"
Datatype: "IBAN2007Identifier" on page 552
Constraints
• IBAN
A valid IBAN consists of all three of the following components: Country Code, check digits and
BBAN.
7.1.2.3.2  Other <Othr>
Presence: [1..1]
Definition: Unique identification of an account, as assigned by the account servicer, using an
identification scheme.
Other <Othr> contains the following elements (see "GenericAccountIdentification1" on page 246 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 247
   SchemeName <SchmeNm> [0..1]  247
{Or     Code <Cd> [1..1] CodeSet 247
Or}     Proprietary <Prtry> [1..1] Text 247
   Issuer <Issr> [0..1] Text 247
7.1.3 Amount
7.1.3.1  AmountAndDirection5
Definition: Amount of money debited or credited on the books of an account servicer.
Approved by the Securities SEG 19 February 2026. Message Items Types
Target2-Securities - Securities and Penalty Reporting 250 March 2026
```

