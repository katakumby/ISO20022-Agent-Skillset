---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["24 camt.046.001.08 GetReservationV08", "24.4 Message Building Blocks", "24.4.2 ReservationQueryDefinition <RsvatnQryDef>", "24.4.2.2 ReservationCriteria <RsvatnCrit>", "24.4.2.2.2 NewCriteria <NewCrit>", "24.4.2.2.2.2 SearchCriteria <SchCrit>", "24.4.2.2.2.2.1 DateTime <DtTm>", "24.4.2.2.2.2.1.2 ToDateTime <ToDtTm>"]
file_pages: [632]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.046.001.08"]
---

# 24.4.2.2.2.2.1.2 ToDateTime <ToDtTm>

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 632 to 632.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 632

```text
Definition: Start date of the range.
Datatype: "ISODateTime" on page 883
24.4.2.2.2.2.1.2  ToDateTime <ToDtTm>
Presence: [1..1]
Definition: End date of the range.
Datatype: "ISODateTime" on page 883
24.4.2.2.2.2.1.3  FromToDateTime <FrToDtTm>
Presence: [1..1]
Definition: Particular time span specified between a start date and an end date.
FromToDateTime <FrToDtTm> contains the following elements (see "DateTimePeriod1" on
page 801 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FromDateTime <FrDtTm> [1..1] DateTime 802
   ToDateTime <ToDtTm> [1..1] DateTime 802
24.4.2.2.2.2.1.4  EqualDateTime <EQDtTm>
Presence: [1..1]
Definition: Specified date to match.
Datatype: "ISODateTime" on page 883
24.4.2.2.2.2.1.5  NotEqualDateTime <NEQDtTm>
Presence: [1..1]
Definition: Specified date to be excluded from the search.
Datatype: "ISODateTime" on page 883
24.4.2.2.2.2.2  SystemIdentification <SysId>
Presence: [0..1]
Definition: Identification of a particular cash clearing system.
SystemIdentification <SysId> contains one of the following elements (see
"SystemIdentification2Choice" on page 846 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   MarketInfrastructureIdentification <MktInfrstrctrId> [1..1] ± 846
Or}   Country <Ctry> [1..1] CodeSet C3 846
24.4.2.2.2.2.3  DefaultReservationType <DfltRsvatnTp>
Presence: [0..*]
Definition: Type of reservation as set by default in the system. The default reservation is applicable by
the system unless otherwise instructed.
Approved by the Payments SEG on 04 February 2025 camt.046.001.08 GetReservationV08
Cash Management - Maintenance 2024 - 2025 632 February 2025
```

