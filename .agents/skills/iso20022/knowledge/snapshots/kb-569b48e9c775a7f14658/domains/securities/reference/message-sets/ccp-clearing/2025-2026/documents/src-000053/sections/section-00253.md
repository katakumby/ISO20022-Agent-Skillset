---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["11 MX secl.010.001.04 SettlementObligationReportV04", "11.4 Message Building Blocks", "11.4.6 ReportDetails <RptDtls>", "11.4.6.2 SettlementObligationDetails <SttlmOblgtnDtls>", "11.4.6.2.9 ClearingAccountType <ClrAcctTp>"]
file_pages: [339]
content_origin: "source-text-extraction"
mentioned_message_ids: ["secl.010.001.04"]
---

# 11.4.6.2.9 ClearingAccountType <ClrAcctTp>

Source: [src-000053](../../../../../../../../../evidence/omitted/4e6ea171978d4b0a5cc40b11.md). Locator: one-based file pages 339 to 339.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 339

```text
CodeName Name Definition
PRIN Principal Trading as Principal.
RISP RisklessPrincipal Trading as a riskless principal, ie, the
order to buy(sell) has been
simultaneously offset by an order to sell
(buy) with another party.
AGEN Agent Trading as Agent on behalf of a
customer.
11.4.6.2.9  ClearingAccountType <ClrAcctTp>
Presence: [0..1]
Definition: Specifies the clearing account type.
Datatype: ClearingAccountType1Code on page 475
CodeName Name Definition
HOUS House Specifies that the account is used to
register trades executed for either the
clearing member or its subsidiaries.
CLIE Client Specifies that the account is used to
register trades executed for the clearing
member's customers.
LIPR LiquidityProvider Specifies that the account is used to
register trades executed for liquidity
providers (also known as market maker)
activities.
11.4.6.2.10  SafekeepingPlace <SfkpgPlc>
Presence: [0..1]
Definition: Place where the securities are safe-kept, physically or notionally. This place can be, for
example, a local custodian, a Central Securities Depository (CSD) or an International Central Securities
Depository (ICSD).
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.010.001.04 SettlementObligationReportV04
March 2026 339
```

