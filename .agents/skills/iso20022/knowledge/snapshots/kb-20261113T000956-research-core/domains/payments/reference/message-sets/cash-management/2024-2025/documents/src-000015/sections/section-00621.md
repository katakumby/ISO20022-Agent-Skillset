---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["37 Message Items Types", "37.1 MessageComponents", "37.1.5 Balance", "37.1.5.1 CashBalance13", "37.1.5.1.6 ProcessingDate <PrcgDt>"]
file_pages: [798]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 37.1.5.1.6 ProcessingDate <PrcgDt>

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 798 to 798.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 798

```text
Definition: Date and time at which the balance is or will be available.
ValueDate <ValDt> contains one of the following elements (see "DateAndDateTime2Choice" on
page 801 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 801
Or}   DateTime <DtTm> [1..1] DateTime 801
37.1.5.1.6  ProcessingDate <PrcgDt>
Presence: [0..1]
Definition: Date or date time when the balance was last updated following an entry posted to the
account, in the books of the account servicing institution.
ProcessingDate <PrcgDt> contains one of the following elements (see "DateAndDateTime2Choice"
on page 801 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 801
Or}   DateTime <DtTm> [1..1] DateTime 801
37.1.5.1.7  NumberOfPayments <NbOfPmts>
Presence: [0..1]
Definition: Number of payments taken into account for the calculation of the cash balance value.
Datatype: "Number" on page 886
37.1.5.1.8  RestrictionType <RstrctnTp>
Presence: [0..1]
Definition: Type providing further information on balance restrictions.
RestrictionType <RstrctnTp> contains the following BalanceRestrictionType1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1] ± 798
   Description <Desc> [0..1] Text 799
   ProcessingType <PrcgTp> [0..1]  799
{Or     Code <Cd> [1..1] CodeSet 799
Or}     Proprietary <Prtry> [1..1] Text 800
37.1.5.1.8.1  Type <Tp>
Presence: [1..1]
Definition: Type of the restriction, for example, selling restriction, buying restriction, placing restriction.
Approved by the Payments SEG on 04 February 2025 Message Items Types
Cash Management - Maintenance 2024 - 2025 798 February 2025
```

