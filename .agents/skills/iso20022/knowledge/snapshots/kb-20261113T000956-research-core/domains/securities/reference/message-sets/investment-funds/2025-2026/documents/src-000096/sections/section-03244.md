---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.16 Direct Debit", "66.1.16.1 DirectDebitMandate7", "66.1.16.1.11 MandateIdentification <MndtId>"]
file_pages: [4480]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.16.1.11 MandateIdentification <MndtId>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4480 to 4480.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4480

```text
Datatype: "Max35Text" on page 5403
66.1.16.1.11  MandateIdentification <MndtId>
Presence: [0..1]
Definition: Reference of the direct debit mandate that has been agreed upon by the debtor and creditor.
Datatype: "Max35Text" on page 5403
66.1.17 Financial Institution Identification
66.1.17.1  FinancialInstitutionIdentification11Choice
Definition: Choice between formats for the identification of the financial institution.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NameAndAddress <NmAndAdr> [1..1] ± 4480
Or   BICFI <BICFI> [1..1] IdentifierSet C5 4480
Or   ClearingSystemMemberIdentification <ClrSysMmbId> [1..1] ± 4481
Or}   ProprietaryIdentification <PrtryId> [1..1]  4481
     Identification <Id> [1..1] Text 4482
66.1.17.1.1  NameAndAddress <NmAndAdr>
Presence: [1..1]
Definition: Identifies the name and (long) postal address of a financial institution.
NameAndAddress <NmAndAdr> contains the following elements (see "NameAndAddress5" on
page 5101 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Name <Nm> [1..1] Text 5101
   Address <Adr> [0..1] ± 5101
66.1.17.1.2  BICFI <BICFI>
Presence: [1..1]
Definition: Identification of the financial institution expressed as a BIC.
Impacted by: C5 "BICFI"
Datatype: "BICFIDec2014Identifier" on page 5390
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4480 May 2026
```

