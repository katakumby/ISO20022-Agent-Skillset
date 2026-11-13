---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["29 sese.035.001.13 SecuritiesFinancingConfirmationV13", "29.4 Message Building Blocks", "29.4.7 SecuritiesFinancingDetails <SctiesFincgDtls>", "29.4.7.27 TerminationAmountPerPieceOfCollateral <TermntnAmtPerPcOfColl>"]
file_pages: [1032]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.035.001.13"]
---

# 29.4.7.27 TerminationAmountPerPieceOfCollateral <TermntnAmtPerPcOfColl>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1032 to 1032.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1032

```text
29.4.7.27  TerminationAmountPerPieceOfCollateral <TermntnAmtPerPcOfColl>
Presence: [0..1]
Definition: Amount of money to be settled per piece of collateral to terminate the transaction.
TerminationAmountPerPieceOfCollateral <TermntnAmtPerPcOfColl> contains the following
elements (see "AmountAndDirection21" on page 1377 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] Amount C2, C8 1377
   CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 1377
29.4.7.28  TerminationTransactionAmount <TermntnTxAmt>
Presence: [0..1]
Definition: Total amount of money to be settled to terminate the transaction.
TerminationTransactionAmount <TermntnTxAmt> contains the following elements (see
"AmountAndDirection21" on page 1377 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] Amount C2, C8 1377
   CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 1377
29.4.7.29  SecondLegNarrative <ScndLegNrrtv>
Presence: [0..1]
Definition: Provides additional information about the second leg in narrative form.
Datatype: "Max140Text" on page 2191
29.4.8 StandingSettlementInstructionDetails
<StgSttlmInstrDtls>
Presence: [0..1]
Definition: Specifies what settlement standing instruction database is to be used to derive the
settlement parties involved in the transaction.
Impacted by: C57 "VendorPresenceRule"
Approved by the Securities SEG on 27 January 2026 sese.035.001.13
SecuritiesFinancingConfirmationV13
Settlement And Reconciliation - Maintenance 2025 - 2026 1032 March 2026
```

