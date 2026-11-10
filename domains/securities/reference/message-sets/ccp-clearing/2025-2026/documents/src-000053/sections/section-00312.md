---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["12 Message Items Types", "12.1 MessageComponents", "12.1.9 Identification Information", "12.1.9.7 GenericIdentification30", "12.1.9.7.2 Issuer <Issr>"]
file_pages: [401]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 12.1.9.7.2 Issuer <Issr>

Source: [src-000053](../../../../../../../../../raw-input/central_counterparty_clearing_ccp_clearing/ISO20022_MDRPart2_CentralCounterPartySecuritiesClearing_Maintenance_2025_2026_v1.pdf). Locator: one-based file pages 401 to 401.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 401

```text
Definition: Proprietary information, often a code, issued by the data source scheme issuer.
Datatype: Exact4AlphaNumericText on page 492
12.1.9.7.2  Issuer <Issr>
Presence: [1..1]
Definition: Entity that assigns the identification.
Datatype: Max35Text on page 493
12.1.9.7.3  SchemeName <SchmeNm>
Presence: [0..1]
Definition: Short textual description of the scheme.
Datatype: Max35Text on page 493
12.1.10 InvestmentFundCashForecast
12.1.10.1  DefaultFund1
Definition: Provides information such as the default fund account identification or the default fund
amount.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   DefaultFundAccount <DfltFndAcct> [1..1] ± 401
   TotalDefaultFundAmount <TtlDfltFndAmt> [1..1] Amount   'C1,
  'C7
402
   Contribution <Cntrbtn> [0..*]  402
     Account <Acct> [0..1] ± 403
     RequiredAmount <ReqrdAmt> [1..1] Amount   'C1,
  'C7
403
     IncreaseCoverageAmount <IncrCvrgAmt> [0..1] Amount   'C1,
  'C7
404
     NonClearingMember <NonClrMmb> [0..1] ± 404
   IncreaseCoverageAmount <IncrCvrgAmt> [0..1] Amount   'C1,
  'C7
405
12.1.10.1.1  DefaultFundAccount <DfltFndAcct>
Presence: [1..1]
Definition: Specifies the account identification of the clearing member at the ICSD (International Central
Securities Depository) or at the central bank.
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
Message Items Types
March 2026 401
```

