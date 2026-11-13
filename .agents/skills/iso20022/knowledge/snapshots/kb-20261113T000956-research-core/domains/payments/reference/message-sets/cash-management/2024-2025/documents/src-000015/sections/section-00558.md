---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["31 camt.070.001.06 ReturnStandingOrderV06", "31.4 Message Building Blocks", "31.4.2 ReportOrError <RptOrErr>", "31.4.2.1 Report <Rpt>", "31.4.2.1.2 StandingOrderOrError <StgOrdrOrErr>", "31.4.2.1.2.1 StandingOrder <StgOrdr>", "31.4.2.1.2.1.19 TotalsPerStandingOrder <TtlsPerStgOrdr>"]
file_pages: [730]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.070.001.06"]
---

# 31.4.2.1.2.1.19 TotalsPerStandingOrder <TtlsPerStgOrdr>

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 730 to 730.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 730

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
31.4.2.1.2.1.19  TotalsPerStandingOrder <TtlsPerStgOrdr>
Presence: [0..1]
Definition: Overall amount of "not yet executed" predefined liquidity transfer orders or "defined" by a
system participant in its sphere of responsibility within the system.
TotalsPerStandingOrder <TtlsPerStgOrdr> contains the following StandingOrderTotalAmount1
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SetPredefinedOrder <SetPrdfndOrdr> [1..1]  730
     TotalAmount <TtlAmt> [1..1] Amount 731
     CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 731
     Currency <Ccy> [0..1] CodeSet C1 731
   PendingPredefinedOrder <PdgPrdfndOrdr> [1..1]  731
     TotalAmount <TtlAmt> [1..1] Amount 732
     CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 732
     Currency <Ccy> [0..1] CodeSet C1 732
   SetStandingOrder <SetStgOrdr> [1..1]  732
     TotalAmount <TtlAmt> [1..1] Amount 733
     CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 733
     Currency <Ccy> [0..1] CodeSet C1 733
   PendingStandingOrder <PdgStgOrdr> [1..1]  733
     TotalAmount <TtlAmt> [1..1] Amount 734
     CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 734
     Currency <Ccy> [0..1] CodeSet C1 734
31.4.2.1.2.1.19.1  SetPredefinedOrder <SetPrdfndOrdr>
Presence: [1..1]
Definition: Total defined amount of predefined liquidity transfer orders.
Approved by the Payments SEG on 04 February 2025 camt.070.001.06 ReturnStandingOrderV06
Cash Management - Maintenance 2024 - 2025 730 February 2025
```

