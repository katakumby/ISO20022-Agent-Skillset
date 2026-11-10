---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["18 camt.019.001.07 ReturnBusinessDayInformationV07", "18.3 Constraints"]
file_pages: [538]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.019.001.07"]
---

# 18.3 Constraints

Source: [src-000015](../../../../../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf). Locator: one-based file pages 538 to 538.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 538

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
               Period <Prd> [0..1]  553
{Or                 FromDateTime <FrDtTm> [1..1] DateTime 553
Or                 ToDateTime <ToDtTm> [1..1] DateTime 553
Or}                 DateTimeRange <DtTmRg> [1..1] ± 553
               Reason <Rsn> [1..1]  554
{Or                 Code <Cd> [1..1] CodeSet 554
Or}                 Proprietary <Prtry> [1..1] Text 554
Or}         BusinessError <BizErr> [1..*]  554
           Error <Err> [1..1]  555
{Or             Code <Cd> [1..1] CodeSet 555
Or}             Proprietary <Prtry> [1..1] Text 555
           Description <Desc> [0..1] Text 555
Or}     OperationalError <OprlErr> [1..*]  555
       Error <Err> [1..1]  556
{Or         Code <Cd> [1..1] CodeSet 556
Or}         Proprietary <Prtry> [1..1] Text 556
       Description <Desc> [0..1] Text 556
   SupplementaryData <SplmtryData> [0..*] ± C3 556
18.3 Constraints
C1 ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the
message containing the currency is exchanged. Valid active currency codes are registered with
the ISO 4217 Maintenance Agency, consist of three (3) contiguous letters, and are not yet
withdrawn on the day the message containing the Currency is exchanged.
C2 Country
The code is checked against the list of country names obtained from the United Nations (ISO
3166, Alpha-2 code).
C3 SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the
RA of ISO 20022 compliant structure(s) to be used in the Envelope element.
18.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
Approved by the Payments SEG on 04 February 2025 camt.019.001.07
ReturnBusinessDayInformationV07
Cash Management - Maintenance 2024 - 2025 538 February 2025
```

