---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["3 acmt.002.001.08 AccountDetailsConfirmationV08", "3.4 Message Building Blocks", "3.4.11 WithdrawalInvestmentPlan <WdrwlInvstmtPlan>"]
file_pages: [52]
content_origin: "source-text-extraction"
mentioned_message_ids: ["acmt.002.001.08"]
---

# 3.4.11 WithdrawalInvestmentPlan <WdrwlInvstmtPlan>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 52 to 52.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 52

```text
SavingsInvestmentPlan <SvgsInvstmtPlan> contains the following elements (see
"InvestmentPlan17" on page 4792 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Frequency <Frqcy> [1..1] ± 4793
   StartDate <StartDt> [0..1] Date 4793
   EndDate <EndDt> [0..1] Date 4793
   Quantity <Qty> [1..1] ± 4793
   GrossAmountIndicator <GrssAmtInd> [0..1] Indicator 4793
   IncomePreference <IncmPref> [0..1] CodeSet 4794
   InitialAmount <InitlAmt> [0..1] ± 4794
   TotalNumberOfInstalments <TtlNbOfInstlmts> [0..1] Quantity 4794
   RoundingDirection <RndgDrctn> [0..1] CodeSet 4794
   SecurityDetails <SctyDtls> [1..50]  4795
     Quantity <Qty> [1..1] ± 4795
     FinancialInstrument <FinInstrm> [1..1] ± C20 4795
     CurrencyOfPlan <CcyOfPlan> [0..1] CodeSet C2 4796
   CashSettlement <CshSttlm> [0..8] ± 4797
   ContractReference <CtrctRef> [0..1] Text 4797
   RelatedContractReference <RltdCtrctRef> [0..1] Text 4798
   ProductIdentification <PdctId> [0..1] Text 4798
   SLAChargeAndCommissionReference
<SLAChrgAndComssnRef>
[0..1] Text 4798
   InsuranceCover <InsrncCover> [0..1] ± 4798
   PlanStatus <PlanSts> [0..1] ± 4798
   InstalmentManagerRole <InstlmtMgrRole> [0..1] ± 4799
Constraints
• AmountRule
If Quantity/Amount is not present, then GrossAmountIndicator is not allowed.
On Condition
    /Quantity/Amount is absent
Following Must be True
    /GrossAmountIndicator Must be absent
3.4.11 WithdrawalInvestmentPlan <WdrwlInvstmtPlan>
Presence: [0..10]
Definition: Confirmation of the information related to a withdrawal plan that is related to the account.
Approved by the Securities SEG on 27 January 2026 acmt.002.001.08 AccountDetailsConfirmationV08
Investment Funds - Maintenance 2025 - 2026 52 May 2026
```

