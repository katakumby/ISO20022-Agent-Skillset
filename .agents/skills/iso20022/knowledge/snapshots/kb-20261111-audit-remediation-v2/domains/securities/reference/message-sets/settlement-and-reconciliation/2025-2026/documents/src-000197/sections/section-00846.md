---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["32 sese.038.001.11 SecuritiesSettlementTransactionModificationRequestV11", "32.4 Message Building Blocks", "32.4.2 UpdateType <UpdTp>", "32.4.2.3 Modification <Mod>", "32.4.2.3.3 TradeDetails <TradDtls>", "32.4.2.3.3.18 MatchingStatus <MtchgSts>"]
file_pages: [1266, 1267]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.038.001.11"]
---

# 32.4.2.3.3.18 MatchingStatus <MtchgSts>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1266 to 1267.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1266

```text
Definition: Account servicer is instructed to buy the indicated currency after the receipt of cash proceeds
or to sell the indicated currency in order to obtain the necessary currency to fund the transaction.
CurrencyToBuyOrSell <CcyToBuyOrSell> contains one of the following elements (see
"CurrencyToBuyOrSell1Choice" on page 1568 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   CurrencyToBuy <CcyToBuy> [1..1] CodeSet C1 1568
Or}   CurrencyToSell <CcyToSell> [1..1] CodeSet C1 1569
32.4.2.3.3.18  MatchingStatus <MtchgSts>
Presence: [0..1]
Definition: Provides the matching status of the instruction.
MatchingStatus <MtchgSts> contains one of the following elements (see "MatchingStatus27Choice"
on page 1924 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1924
Or}   Proprietary <Prtry> [1..1] ± 1925
32.4.2.3.3.19  AffirmationStatus <AffirmSts>
Presence: [0..1]
Definition: Status of affirmation of a trade.
AffirmationStatus <AffirmSts> contains one of the following elements (see
"AffirmationStatus8Choice" on page 1878 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1878
Or}   Proprietary <Prtry> [1..1] ± 1879
32.4.2.3.3.20  FXAdditionalDetails <FxAddtlDtls>
Presence: [0..1]
Definition: Provides additional details pertaining to foreign exchange instructions.
Datatype: "Max350Text" on page 2192
32.4.2.3.3.21  SettlementInstructionProcessingAdditionalDetails <SttlmInstrPrcgAddtlDtls>
Presence: [0..1]
Definition: Provides additional settlement processing information which can not be included within the
structured fields of the message.
Datatype: "Max350Text" on page 2192
32.4.2.3.4  FinancialInstrumentIdentification <FinInstrmId>
Presence: [0..1]
Approved by the Securities SEG on 27 January 2026 sese.038.001.11
SecuritiesSettlementTransactionModificationReques
tV11
Settlement And Reconciliation - Maintenance 2025 - 2026 1266 March 2026
```

## File page 1267

```text
Definition: Financial instrument representing a sum of rights of the investor vis-a-vis the issuer.
Impacted by: C21 "DescriptionPresenceRule", C22 "DescriptionUsageRule", C29 "ISINGuideline", C30
"ISINPresenceRule", C40 "OtherIdentificationPresenceRule"
FinancialInstrumentIdentification <FinInstrmId> contains the following elements (see
"SecurityIdentification19" on page 1474 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ISIN <ISIN> [0..1] IdentifierSet 1475
   OtherIdentification <OthrId> [0..*]  1475
     Identification <Id> [1..1] Text 1475
     Suffix <Sfx> [0..1] Text 1475
     Type <Tp> [1..1] ± 1476
   Description <Desc> [0..1] Text 1476
Constraints
• DescriptionPresenceRule
If Description is not present then either ISIN or at least one occurrence of OtherIdentification must be
present.
On Condition
    /Description is absent
Following Must be True
    /ISIN Must be present
 Or    /OtherIdentification[*] Must be present
• DescriptionUsageRule
Description must be used alone as the last resort.
• ISINGuideline
When an ISIN code exists, it is strongly recommended that the ISIN be used.
• ISINPresenceRule
If ISIN is not present then either Description or at least one occurrence of OtherIdentification must be
present.
On Condition
    /ISIN is absent
Following Must be True
    /OtherIdentification[*] Must be present
 Or    /Description Must be present
• OtherIdentificationPresenceRule
If OtherIdentification is not present then either ISIN or Description must be present.
On Condition
    /OtherIdentification[*] is absent
Following Must be True
    /ISIN Must be present
 Or    /Description Must be present
Approved by the Securities SEG on 27 January 2026 sese.038.001.11
SecuritiesSettlementTransactionModificationReques
tV11
Settlement And Reconciliation - Maintenance 2025 - 2026 1267 March 2026
```

