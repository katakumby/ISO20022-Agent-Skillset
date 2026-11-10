---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S IntraBalanceMovement"
source_ids: ["src-000360"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["9 camt.078.001.02 IntraBalanceMovementQueryV02", "9.4 Message Building Blocks", "9.4.2 QueryDefinition <QryDef>", "9.4.2.2 SearchCriteria <SchCrit>", "9.4.2.2.10 SettlementCurrency <SttlmCcy>"]
file_pages: [180]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.078.001.02"]
---

# 9.4.2.2.10 SettlementCurrency <SttlmCcy>

Source: [src-000360](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart2_Target2Securities_IntraBalanceMovement_2023_2024_v1.pdf`. Locator: one-based file pages 180 to 180.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 180

```text
SettledAmount <SttldAmt> contains one of the following elements (see
"ImpliedCurrencyAmountRange1Choice" on page 394 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   FromAmount <FrAmt> [1..1] ± 394
Or   ToAmount <ToAmt> [1..1] ± 394
Or   FromToAmount <FrToAmt> [1..1]  394
     FromAmount <FrAmt> [1..1] ± 395
     ToAmount <ToAmt> [1..1] ± 395
Or   EqualAmount <EQAmt> [1..1] Amount 395
Or}   NotEqualAmount <NEQAmt> [1..1] Amount 395
9.4.2.2.10  SettlementCurrency <SttlmCcy>
Presence: [0..*]
Definition: Currency in which the instructed amount is expressed.
Impacted by: C2 "ActiveOrHistoricCurrency"
Datatype: "ActiveOrHistoricCurrencyCode" on page 475
Constraints
• ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the Currency
is exchanged.
9.4.2.2.11  IntendedSettlementDate <IntnddSttlmDt>
Presence: [0..1]
Definition: Date and time at which the amount of money is intended to be moved.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
camt.078.001.02 IntraBalanceMovementQueryV02
Target2-Securities - Intra-balance Movement - Maintenance
2023 - 2024
180 March 2024
```

