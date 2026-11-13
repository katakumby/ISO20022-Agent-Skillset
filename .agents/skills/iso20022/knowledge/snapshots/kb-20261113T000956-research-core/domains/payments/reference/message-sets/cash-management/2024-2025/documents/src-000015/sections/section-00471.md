---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["24 camt.046.001.08 GetReservationV08", "24.4 Message Building Blocks", "24.4.2 ReservationQueryDefinition <RsvatnQryDef>", "24.4.2.2 ReservationCriteria <RsvatnCrit>", "24.4.2.2.2 NewCriteria <NewCrit>", "24.4.2.2.2.2 SearchCriteria <SchCrit>"]
file_pages: [631]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.046.001.08"]
---

# 24.4.2.2.2.2 SearchCriteria <SchCrit>

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 631 to 631.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 631

```text
24.4.2.2.2.2  SearchCriteria <SchCrit>
Presence: [0..*]
Definition: Defines the criteria to extract the reservation information.
SearchCriteria <SchCrit> contains the following ReservationSearchCriteria6 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   DateTime <DtTm> [0..1]  631
{Or     FromDateTime <FrDtTm> [1..1] DateTime 631
Or     ToDateTime <ToDtTm> [1..1] DateTime 632
Or     FromToDateTime <FrToDtTm> [1..1] ± 632
Or     EqualDateTime <EQDtTm> [1..1] DateTime 632
Or}     NotEqualDateTime <NEQDtTm> [1..1] DateTime 632
   SystemIdentification <SysId> [0..1] ± 632
   DefaultReservationType <DfltRsvatnTp> [0..*]  632
{Or     Code <Cd> [1..1] CodeSet 633
Or}     Proprietary <Prtry> [1..1] Text 633
   CurrentReservationType <CurRsvatnTp> [0..*]  633
{Or     Code <Cd> [1..1] CodeSet 633
Or}     Proprietary <Prtry> [1..1] Text 633
   AccountOwner <AcctOwnr> [0..1] ± 633
   AccountIdentification <AcctId> [0..1] ± 634
24.4.2.2.2.2.1  DateTime <DtTm>
Presence: [0..1]
Definition: Patterns to search a date time.
DateTime <DtTm> contains one of the following DateTimeSearch2Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   FromDateTime <FrDtTm> [1..1] DateTime 631
Or   ToDateTime <ToDtTm> [1..1] DateTime 632
Or   FromToDateTime <FrToDtTm> [1..1] ± 632
Or   EqualDateTime <EQDtTm> [1..1] DateTime 632
Or}   NotEqualDateTime <NEQDtTm> [1..1] DateTime 632
24.4.2.2.2.2.1.1  FromDateTime <FrDtTm>
Presence: [1..1]
Approved by the Payments SEG on 04 February 2025 camt.046.001.08 GetReservationV08
Cash Management - Maintenance 2024 - 2025 631 February 2025
```

