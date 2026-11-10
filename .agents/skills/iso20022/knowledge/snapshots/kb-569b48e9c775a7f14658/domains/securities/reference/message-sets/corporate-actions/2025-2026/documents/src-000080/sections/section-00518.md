---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["9 seev.037.001.17 CorporateActionMovementReversalAdviceV17", "9.4 Message Building Blocks", "9.4.9 CorporateActionConfirmationDetails <CorpActnConfDtls>", "9.4.9.1 OptionNumber <OptnNb>"]
file_pages: [682]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.037.001.17"]
---

# 9.4.9.1 OptionNumber <OptnNb>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 682 to 682.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 682

```text
CorporateActionConfirmationDetails <CorpActnConfDtls> contains the following
CorporateActionOption240 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   OptionNumber <OptnNb> [1..1] ± 682
   OptionType <OptnTp> [1..1] ± 682
   SecuritiesMovementDetails <SctiesMvmntDtls> [0..*]  683
     FinancialInstrumentIdentification <FinInstrmId> [1..1] ± C7, C8,
C13,
C14,
C18
683
     CreditDebitIndicator <CdtDbtInd> [1..1] CodeSet 684
     PostingQuantity <PstngQty> [1..1] ± 684
     PostingDate <PstngDt> [1..1] ± 685
     OriginalPostingDate <OrgnlPstngDt> [0..1] ± 685
   CashMovementDetails <CshMvmntDtls> [0..*]  685
     CreditDebitIndicator <CdtDbtInd> [1..1] CodeSet 686
     Account <Acct> [0..1]  686
{Or       CashAccount <CshAcct> [1..1] ± 686
Or       ChargesAccount <ChrgsAcct> [1..1] ± 687
Or}       TaxAccount <TaxAcct> [1..1] ± 687
     PostingDate <PstngDt> [1..1] ± 687
     OriginalPostingDate <OrgnlPstngDt> [0..1] ± 687
     ValueDate <ValDt> [0..1] Date 688
     PostingAmount <PstngAmt> [1..1] Amount C1, C6 688
9.4.9.1  OptionNumber <OptnNb>
Presence: [1..1]
Definition: Number identifying the available corporate action options.
OptionNumber <OptnNb> contains one of the following elements (see "OptionNumber1Choice" on
page 970 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Number <Nb> [1..1] Text 970
Or}   Code <Cd> [1..1] CodeSet 970
9.4.9.2  OptionType <OptnTp>
Presence: [1..1]
Approved by the Securities SEG on 27 January 2026 seev.037.001.17
CorporateActionMovementReversalAdviceV17
Corporate Actions - Maintenance 2025 - 2026 682 February 2026
```

