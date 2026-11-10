---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["3 semt.026.001.01 SecuritiesSettlementTransactionQueryV01", "3.4 Message Building Blocks", "3.4.1 QueryDefinition <QryDef>", "3.4.1.2 SearchCriteria <SchCrit>", "3.4.1.2.16 EffectiveSettlementDate <FctvSttlmDt>", "3.4.1.2.16.2 DateTime <DtTm>", "3.4.1.2.16.2.3 FromToDateTime <FrToDtTm>"]
file_pages: [66]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.026.001.01"]
---

# 3.4.1.2.16.2.3 FromToDateTime <FrToDtTm>

Source: [src-000375](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 66 to 66.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 66

```text
3.4.1.2.16.2.3  FromToDateTime <FrToDtTm>
Presence: [1..1]
Definition: Particular time span specified between a start date and an end date.
FromToDateTime <FrToDtTm> contains the following elements (see "DateTimePeriod1" on page 323
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FromDateTime <FrDtTm> [1..1] DateTime 323
   ToDateTime <ToDtTm> [1..1] DateTime 324
3.4.1.2.16.2.4  EqualDateTime <EQDtTm>
Presence: [1..1]
Definition: Specified date to match.
Datatype: "ISODateTime" on page 551
3.4.1.2.16.2.5  NotEqualDateTime <NEQDtTm>
Presence: [1..1]
Definition: Specified date to be excluded from the search.
Datatype: "ISODateTime" on page 551
3.4.1.2.17  SettlementCurrency <SttlmCcy>
Presence: [0..*]
Definition: Currency in which the instructed amount is expressed.
Impacted by: C2 "ActiveOrHistoricCurrency"
Datatype: "ActiveOrHistoricCurrencyCode" on page 492
Constraints
• ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the Currency
is exchanged.
3.4.1.2.18  SafekeepingAccountOwner <SfkpgAcctOwnr>
Presence: [0..*]
Definition: Party that owns the account.
Approved by the Securities SEG 19 February 2026. semt.026.001.01
SecuritiesSettlementTransactionQueryV01
Target2-Securities - Securities and Penalty Reporting 66 March 2026
```

