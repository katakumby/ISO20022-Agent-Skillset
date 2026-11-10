---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["9 seev.037.001.17 CorporateActionMovementReversalAdviceV17", "9.4 Message Building Blocks", "9.4.9 CorporateActionConfirmationDetails <CorpActnConfDtls>", "9.4.9.3 SecuritiesMovementDetails <SctiesMvmntDtls>"]
file_pages: [683]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.037.001.17"]
---

# 9.4.9.3 SecuritiesMovementDetails <SctiesMvmntDtls>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 683 to 683.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 683

```text
Definition: Specifies the corporate action options available to the account owner.
OptionType <OptnTp> contains one of the following elements (see "CorporateActionOption33Choice"
on page 944 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 944
Or}   Proprietary <Prtry> [1..1] ± 945
9.4.9.3  SecuritiesMovementDetails <SctiesMvmntDtls>
Presence: [0..*]
Definition: Provides information about the securities movement linked to the corporate action option.
SecuritiesMovementDetails <SctiesMvmntDtls> contains the following SecuritiesOption80
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FinancialInstrumentIdentification <FinInstrmId> [1..1] ± C7, C8,
C13,
C14,
C18
683
   CreditDebitIndicator <CdtDbtInd> [1..1] CodeSet 684
   PostingQuantity <PstngQty> [1..1] ± 684
   PostingDate <PstngDt> [1..1] ± 685
   OriginalPostingDate <OrgnlPstngDt> [0..1] ± 685
9.4.9.3.1  FinancialInstrumentIdentification <FinInstrmId>
Presence: [1..1]
Definition: Identification of the financial instrument.
Impacted by: C7 "DescriptionPresenceRule", C8 "DescriptionUsageRule", C13 "ISINGuideline", C14
"ISINPresenceRule", C18 "OtherIdentificationPresenceRule"
FinancialInstrumentIdentification <FinInstrmId> contains the following elements (see
"SecurityIdentification19" on page 869 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ISIN <ISIN> [0..1] IdentifierSet 870
   OtherIdentification <OthrId> [0..*]  870
     Identification <Id> [1..1] Text 870
     Suffix <Sfx> [0..1] Text 870
     Type <Tp> [1..1] ± 871
   Description <Desc> [0..1] Text 871
Approved by the Securities SEG on 27 January 2026 seev.037.001.17
CorporateActionMovementReversalAdviceV17
Corporate Actions - Maintenance 2025 - 2026 683 February 2026
```

