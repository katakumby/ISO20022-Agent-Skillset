---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["4 acmt.003.001.08 AccountModificationInstructionV08", "4.4 Message Building Blocks", "4.4.12 ModifiedCashSettlement <ModfdCshSttlm>"]
file_pages: [73]
content_origin: "source-text-extraction"
mentioned_message_ids: ["acmt.003.001.08"]
---

# 4.4.12 ModifiedCashSettlement <ModfdCshSttlm>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 73 to 73.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 73

```text
ModifiedWithdrawalInvestmentPlan <ModfdWdrwlInvstmtPlan> contains the following elements
(see "ModificationScope41" on page 4743 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ModificationScopeIndication <ModScpIndctn> [1..1] CodeSet 4744
   InvestmentPlan <InvstmtPlan> [1..1]  C6 4745
     Frequency <Frqcy> [1..1] ± 4746
     StartDate <StartDt> [0..1] Date 4746
     EndDate <EndDt> [0..1] Date 4746
     Quantity <Qty> [1..1] ± 4746
     GrossAmountIndicator <GrssAmtInd> [0..1] Indicator 4746
     IncomePreference <IncmPref> [0..1] CodeSet 4747
     InitialAmount <InitlAmt> [0..1] ± 4747
     TotalNumberOfInstalments <TtlNbOfInstlmts> [0..1] Quantity 4747
     RoundingDirection <RndgDrctn> [0..1] CodeSet 4747
     SecurityDetails <SctyDtls> [1..50]  4747
       Quantity <Qty> [1..1] ± 4748
       FinancialInstrument <FinInstrm> [1..1] ± C20 4748
       CurrencyOfPlan <CcyOfPlan> [0..1] CodeSet C2 4749
     ModifiedCashSettlement <ModfdCshSttlm> [0..8] ± 4750
     ContractReference <CtrctRef> [0..1] Text 4751
     RelatedContractReference <RltdCtrctRef> [0..1] Text 4751
     ProductIdentification <PdctId> [0..1] Text 4751
     SLAChargeAndCommissionReference
<SLAChrgAndComssnRef>
[0..1] Text 4751
     InsuranceCover <InsrncCover> [0..1] ± 4751
     PlanStatus <PlanSts> [0..1] ± 4751
     InstalmentManagerRole <InstlmtMgrRole> [0..1] ± 4752
4.4.12 ModifiedCashSettlement <ModfdCshSttlm>
Presence: [0..8]
Definition: Cash settlement standing instruction to be either inserted or deleted.
Approved by the Securities SEG on 27 January 2026 acmt.003.001.08 AccountModificationInstructionV08
Investment Funds - Maintenance 2025 - 2026 73 May 2026
```

