---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["4 camt.005.001.11 GetTransactionV11", "4.4 Message Building Blocks", "4.4.2 TransactionQueryDefinition <TxQryDef>", "4.4.2.2 TransactionCriteria <TxCrit>", "4.4.2.2.2 NewCriteria <NewCrit>", "4.4.2.2.2.2 SearchCriteria <SchCrit>", "4.4.2.2.2.2.1 PaymentTo <PmtTo>"]
file_pages: [135]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.005.001.11"]
---

# 4.4.2.2.2.2.1 PaymentTo <PmtTo>

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 135 to 135.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 135

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
Or         ToDateTime <ToDtTm> [1..1] DateTime 189
Or}         DateTimeRange <DtTmRg> [1..1] ± 189
Or}       DateSearch <DtSch> [1..1]  189
{Or         FromDate <FrDt> [1..1] Date 190
Or         ToDate <ToDt> [1..1] Date 190
Or         FromToDate <FrToDt> [1..1] ± 190
Or         EqualDate <EQDt> [1..1] Date 190
Or}         NotEqualDate <NEQDt> [1..1] Date 190
     AccountOwner <AcctOwnr> [0..1] ± 190
     AccountServicer <AcctSvcr> [0..1] ± 191
4.4.2.2.2.2.1  PaymentTo <PmtTo>
Presence: [0..*]
Definition: Defines the criteria which are used to search for the destination of the payment.
PaymentTo <PmtTo> contains the following SystemSearch5 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SystemIdentification <SysId> [0..*]  135
{Or     Code <Cd> [1..1] CodeSet 135
Or}     Proprietary <Prtry> [1..1] Text 136
   MemberIdentification <MmbId> [0..*] ± 136
   Country <Ctry> [0..1] CodeSet C5 136
   AccountIdentification <AcctId> [0..1] ± 137
4.4.2.2.2.2.1.1  SystemIdentification <SysId>
Presence: [0..*]
Definition: Identification of a particular cash clearing system.
SystemIdentification <SysId> contains one of the following ClearingSystemIdentification3Choice
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 135
Or}   Proprietary <Prtry> [1..1] Text 136
4.4.2.2.2.2.1.1.1  Code <Cd>
Presence: [1..1]
Approved by the Payments SEG on 04 February 2025 camt.005.001.11 GetTransactionV11
Cash Management - Maintenance 2024 - 2025 135 February 2025
```

