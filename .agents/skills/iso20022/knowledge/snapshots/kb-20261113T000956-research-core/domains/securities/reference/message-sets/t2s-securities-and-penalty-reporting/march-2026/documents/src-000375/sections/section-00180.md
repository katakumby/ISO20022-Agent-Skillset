---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.2 Account Identification"]
file_pages: [248]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.2 Account Identification

Source: [src-000375](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 248 to 248.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 248

```text
7.1.2 Account Identification
7.1.2.1  CashAccountIdentification5Choice
Definition: Unique identifier of an account, as assigned by the account servicer.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   IBAN <IBAN> [1..1] IdentifierSet C8 248
Or}   Proprietary <Prtry> [1..1] Text 248
7.1.2.1.1  IBAN <IBAN>
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
7.1.2.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Unique identifier for an account. It is assigned by the account servicer using a proprietary
identification scheme.
Datatype: "Max34Text" on page 557
7.1.2.2  SecuritiesAccount2Choice
Definition: Specifies one or a range of securities accounts.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Range <Rg> [1..1]  248
     From <Fr> [1..1] ± 249
     To <To> [1..1] ± 249
Or}   Account <Acct> [1..*] ± 249
7.1.2.2.1  Range <Rg>
Presence: [1..1]
Definition: Range of identifications of the securities accounts.
Approved by the Securities SEG 19 February 2026. Message Items Types
Target2-Securities - Securities and Penalty Reporting 248 March 2026
```

