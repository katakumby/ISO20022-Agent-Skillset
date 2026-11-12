---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["3 camt.004.001.10 ReturnAccountV10", "3.4 Message Building Blocks", "3.4.2 ReportOrError <RptOrErr>", "3.4.2.1 AccountReport <AcctRpt>", "3.4.2.1.2 AccountOrError <AcctOrErr>", "3.4.2.1.2.1 Account <Acct>", "3.4.2.1.2.1.10 StandingOrder <StgOrdr>", "3.4.2.1.2.1.10.19 TotalsPerStandingOrder <TtlsPerStgOrdr>"]
file_pages: [90]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.004.001.10"]
---

# 3.4.2.1.2.1.10.19 TotalsPerStandingOrder <TtlsPerStgOrdr>

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 90 to 90.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 90

```text
Constraints
• IdentificationAndProxyGuideline
If the account identification is not defined through a conventional identification such as an email
address or a mobile number, then the proxy element should be used for the identification of the
account.
• IdentificationOrProxyPresenceRule
Identification must be present or Proxy must be present. Both may be present.
Following Must be True
    /Identification Must be present
 Or    /Proxy Must be present
3.4.2.1.2.1.10.19  TotalsPerStandingOrder <TtlsPerStgOrdr>
Presence: [0..1]
Definition: Overall amount of "not yet executed" predefined liquidity transfer orders or "defined" by a
system participant in its sphere of responsibility within the system.
TotalsPerStandingOrder <TtlsPerStgOrdr> contains the following StandingOrderTotalAmount1
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SetPredefinedOrder <SetPrdfndOrdr> [1..1]  90
     TotalAmount <TtlAmt> [1..1] Amount 91
     CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 91
     Currency <Ccy> [0..1] CodeSet C1 91
   PendingPredefinedOrder <PdgPrdfndOrdr> [1..1]  91
     TotalAmount <TtlAmt> [1..1] Amount 92
     CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 92
     Currency <Ccy> [0..1] CodeSet C1 92
   SetStandingOrder <SetStgOrdr> [1..1]  92
     TotalAmount <TtlAmt> [1..1] Amount 93
     CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 93
     Currency <Ccy> [0..1] CodeSet C1 93
   PendingStandingOrder <PdgStgOrdr> [1..1]  93
     TotalAmount <TtlAmt> [1..1] Amount 94
     CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 94
     Currency <Ccy> [0..1] CodeSet C1 94
3.4.2.1.2.1.10.19.1  SetPredefinedOrder <SetPrdfndOrdr>
Presence: [1..1]
Definition: Total defined amount of predefined liquidity transfer orders.
Approved by the Payments SEG on 04 February 2025 camt.004.001.10 ReturnAccountV10
Cash Management - Maintenance 2024 - 2025 90 February 2025
```

