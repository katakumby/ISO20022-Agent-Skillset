---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["10 camt.011.001.08 ModifyLimitV08", "10.3 Constraints"]
file_pages: [424]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.011.001.08"]
---

# 10.3 Constraints

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 424 to 424.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 424

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
{Or           Code <Cd> [1..1] CodeSet 443
Or}           Proprietary <Prtry> [1..1] Text 445
         AccountOwner <AcctOwnr> [0..1] ± 445
         AccountIdentification <AcctId> [0..1] ± 446
     NewLimitValueSet <NewLmtValSet> [1..1]  446
       StartDateTime <StartDtTm> [0..1] ± 447
       Amount <Amt> [1..1] ± 447
       CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 447
     OldLimitValueSet <OdLmtValSet> [0..1]  447
       Amount <Amt> [1..1] ± 447
       CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 448
     LimitValueAmendment <LmtValAmdmnt> [0..1]  448
{Or       IncreaseAmount <IncrAmt> [1..1] ± 448
Or}       DecreaseAmount <DcrAmt> [1..1] ± 448
   SupplementaryData <SplmtryData> [0..*] ± C9 449
10.3 Constraints
C1 ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the
message containing the currency is exchanged. Valid active currency codes are registered with
the ISO 4217 Maintenance Agency, consist of three (3) contiguous letters, and are not yet
withdrawn on the day the message containing the Currency is exchanged.
C2 BICFI
Valid BICs for financial institutions are registered and published by the ISO 9362 Registration
Authority in the ISO directory of BICs, and consist of eight (8) or eleven (11) contiguous
characters.
C3 BilateralLimitCounterparty1Rule
If Type is MULT, then BilateralLimitCounterpartyIdentification is not allowed.
C4 BilateralLimitCounterparty2Rule
If Type is BILI or NELI or INBI, then BilateralLimitCounterpartyIdentification must be present.
C5 Country
The code is checked against the list of country names obtained from the United Nations (ISO
3166, Alpha-2 code).
Approved by the Payments SEG on 04 February 2025 camt.011.001.08 ModifyLimitV08
Cash Management - Maintenance 2024 - 2025 424 February 2025
```

