---
template: false
document_kind: "message-mdr-evidence"
review_status: "needs-review"
domain: "securities"
message_id: "sese.007.001.10"
message_family: "sese.007"
namespace: "urn:iso:std:iso:20022:tech:xsd:sese.007.001.10"
source_ids: ["src-000096"]
source_locations: [{"source_id": "src-000096", "heading": "30 sese.007.001.10 TransferInConfirmationV10", "file_pages": [695, 777]}]
limitations: ["PDF text and candidate tables require visual reconciliation; business-role mapping is not inferred from XML names.", "Separate publication statements are retained without version-comparison or silent conflict resolution."]
source_editions: ["May 2026"]
---

# sese.007.001.10 MDR business evidence

The following supplied publications explicitly define this exact message identifier. Functionality text is retained with page locators; detailed definitions, rules, tables and figures remain in focused source sections. This page does not substitute one message version for another.

## src-000096 — 30 sese.007.001.10 TransferInConfirmationV10

[src-000096](../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md); file pp695–777; publication May 2026. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000096, 30 sese.007.001.10 TransferInConfirmationV10, Functionality, file p695.**

Scope
The TransferInConfirmation message is sent by an executing party, for example, a transfer agent, to the
instructing party, for example, an investment manager or its authorised representative, to confirm the
receipt of a financial instrument, free of payment, on a given date, from a specified party.
This message may also be used to confirm the receipt of a financial instrument, free of payment, from
another of the instructing parties own accounts or from a third party.
This message may also be used as an advice, that is, the message is used to provide account
information.
Usage
The TransferInConfirmation message is used to confirm receipt of a financial instrument, either from
another account owned by the instructing party or from a third party. The reference of the transfer
confirmation is identified in TransferConfirmationReference.
The reference of the original transfer instruction is specified in TransferReference. The message
identification of the TransferInInstruction message in which the transfer instruction was conveyed may
also be quoted in RelatedReference.
Outline
The TransferInConfirmationV10 MessageDefinition is composed of 12 MessageBuildingBlocks:
A. MessageIdentification
Reference that uniquely identifies the message from a business application standpoint.
B. PoolReference
Collective reference identifying a set of messages.
C. PreviousReference
Reference to a linked message that was previously sent.
D. RelatedReference
Reference to a linked message that was previously received.
E. Function
Function of the transfer in, that is, whether the transfer in message is used as a confirmation or as
or an advice. The absence of Function indicates the message is a confirmation.
F. MasterReference
Unique and unambiguous identifier for a group of individual transfers as assigned by the instructing
party. This identifier links the individual transfers together.
G. TransferDetails
Approved by the Securities SEG on 27 January 2026 sese.007.001.10 TransferInConfirmationV10
Investment Funds - Maintenance 2025 - 2026 695 May 2026

**src-000096, 30 sese.007.001.10 TransferInConfirmationV10, Functionality, file p696.**

General information related to the transfer of the financial instrument.
H. AccountDetails
Information related to the account into which the financial instrument was received.
I. SettlementDetails
Information related to the delivering side of the transfer.
J. MarketPracticeVersion
Identifies the market practice to which the message conforms.
K. CopyDetails
Information provided when the message is a copy of a previous message.
L. Extension
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities SEG on 27 January 2026 sese.007.001.10 TransferInConfirmationV10
Investment Funds - Maintenance 2025 - 2026 696 May 2026

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/investment-funds/2025-2026/documents/src-000096/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [30 sese.007.001.10 TransferInConfirmationV10](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00513.md) | 695–696 |
| [30 sese.007.001.10 TransferInConfirmationV10 / 30.2 Structure](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00514.md) | 697–702 |
| [30 sese.007.001.10 TransferInConfirmationV10 / 30.3 Constraints](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00515.md); [Constraints continuation C31–C35 (file p706)](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00516.md#file-page-706) | 703–705 |
| [30 sese.007.001.10 TransferInConfirmationV10 / 30.4 Message Building Blocks](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00516.md) | 706–706 |
| [30 sese.007.001.10 TransferInConfirmationV10 / 30.4 Message Building Blocks / 30.4.3 PreviousReference &lt;PrvsRef&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00517.md) | 707–711 |
| [30 sese.007.001.10 TransferInConfirmationV10 / 30.4 Message Building Blocks / 30.4.4 RelatedReference &lt;RltdRef&gt; / 30.4.7.1 TransferConfirmationReference &lt;TrfConfRef&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00518.md) | 712–712 |
| [30 sese.007.001.10 TransferInConfirmationV10 / 30.4 Message Building Blocks / 30.4.4 RelatedReference &lt;RltdRef&gt; / 30.4.7.3 ClientReference &lt;ClntRef&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00519.md) | 713–713 |
| [30 sese.007.001.10 TransferInConfirmationV10 / 30.4 Message Building Blocks / 30.4.4 RelatedReference &lt;RltdRef&gt; / 30.4.7.6 RequestedSettlementDate &lt;ReqdSttlmDt&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00520.md) | 714–714 |
| [30 sese.007.001.10 TransferInConfirmationV10 / 30.4 Message Building Blocks / 30.4.4 RelatedReference &lt;RltdRef&gt; / 30.4.7.11 TransferReason &lt;TrfRsn&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00521.md) | 715–716 |
| [30 sese.007.001.10 TransferInConfirmationV10 / 30.4 Message Building Blocks / 30.4.4 RelatedReference &lt;RltdRef&gt; / 30.4.7.13 FinancialInstrumentDetails &lt;FinInstrmDtls&gt; / 30.4.7.13.1 Identification &lt;Id&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00522.md) | 717–717 |
| [30 sese.007.001.10 TransferInConfirmationV10 / 30.4 Message Building Blocks / 30.4.4 RelatedReference &lt;RltdRef&gt; / 30.4.7.13 FinancialInstrumentDetails &lt;FinInstrmDtls&gt; / 30.4.7.13.1 Identification &lt;Id&gt; / 30.4.7.13.1.3 CUSIP &lt;CUSIP&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00523.md) | 718–718 |
| [30 sese.007.001.10 TransferInConfirmationV10 / 30.4 Message Building Blocks / 30.4.4 RelatedReference &lt;RltdRef&gt; / 30.4.7.13 FinancialInstrumentDetails &lt;FinInstrmDtls&gt; / 30.4.7.13.1 Identification &lt;Id&gt; / 30.4.7.13.1.10 Dutch &lt;Dtch&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00524.md) | 719–719 |
| [30 sese.007.001.10 TransferInConfirmationV10 / 30.4 Message Building Blocks / 30.4.4 RelatedReference &lt;RltdRef&gt; / 30.4.7.13 FinancialInstrumentDetails &lt;FinInstrmDtls&gt; / 30.4.7.13.1 Identification &lt;Id&gt; / 30.4.7.13.1.16 OtherProprietaryIdentification &lt;OthrPrtryId&gt; / 30.4.7.13.1.16.1 Identification &lt;Id&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00525.md) | 720–720 |
| [30 sese.007.001.10 TransferInConfirmationV10 / 30.4 Message Building Blocks / 30.4.4 RelatedReference &lt;RltdRef&gt; / 30.4.7.13 FinancialInstrumentDetails &lt;FinInstrmDtls&gt; / 30.4.7.13.6 SecuritiesForm &lt;SctiesForm&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00526.md) | 721–721 |
| [30 sese.007.001.10 TransferInConfirmationV10 / 30.4 Message Building Blocks / 30.4.4 RelatedReference &lt;RltdRef&gt; / 30.4.7.14 TotalUnitsNumber &lt;TtlUnitsNb&gt; / 30.4.7.14.1 UnitsNumber &lt;UnitsNb&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00527.md) | 722–724 |
| [30 sese.007.001.10 TransferInConfirmationV10 / 30.4 Message Building Blocks / 30.4.4 RelatedReference &lt;RltdRef&gt; / 30.4.7.16 UnitsDetails &lt;UnitsDtls&gt; / 30.4.7.16.1 Units &lt;Units&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00528.md) | 725–725 |
| [30 sese.007.001.10 TransferInConfirmationV10 / 30.4 Message Building Blocks / 30.4.4 RelatedReference &lt;RltdRef&gt; / 30.4.7.16 UnitsDetails &lt;UnitsDtls&gt; / 30.4.7.16.6 Reference &lt;Ref&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00529.md) | 726–727 |
| [30 sese.007.001.10 TransferInConfirmationV10 / 30.4 Message Building Blocks / 30.4.4 RelatedReference &lt;RltdRef&gt; / 30.4.7.16 UnitsDetails &lt;UnitsDtls&gt; / 30.4.7.16.8 TransactionOverhead &lt;TxOvrhd&gt; / 30.4.7.16.8.1 TotalOverheadApplied &lt;TtlOvrhdApld&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00530.md) | 728–728 |
| [30 sese.007.001.10 TransferInConfirmationV10 / 30.4 Message Building Blocks / 30.4.4 RelatedReference &lt;RltdRef&gt; / 30.4.7.16 UnitsDetails &lt;UnitsDtls&gt; / 30.4.7.16.8 TransactionOverhead &lt;TxOvrhd&gt; / 30.4.7.16.8.2 TotalFees &lt;TtlFees&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00531.md) | 729–729 |
| [30 sese.007.001.10 TransferInConfirmationV10 / 30.4 Message Building Blocks / 30.4.4 RelatedReference &lt;RltdRef&gt; / 30.4.7.16 UnitsDetails &lt;UnitsDtls&gt; / 30.4.7.16.8 TransactionOverhead &lt;TxOvrhd&gt; / 30.4.7.16.8.5 IndividualFee &lt;IndvFee&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00532.md) | 730–730 |
| [30 sese.007.001.10 TransferInConfirmationV10 / 30.4 Message Building Blocks / 30.4.4 RelatedReference &lt;RltdRef&gt; / 30.4.7.16 UnitsDetails &lt;UnitsDtls&gt; / 30.4.7.16.8 TransactionOverhead &lt;TxOvrhd&gt; / 30.4.7.16.8.5 IndividualFee &lt;IndvFee&gt; / 30.4.7.16.8.5.1 Type &lt;Tp&gt; / 30.4.7.16.8.5.1.1 Code &lt;Cd&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00533.md) | 731–731 |
| [30 sese.007.001.10 TransferInConfirmationV10 / 30.4 Message Building Blocks / 30.4.4 RelatedReference &lt;RltdRef&gt; / 30.4.7.16 UnitsDetails &lt;UnitsDtls&gt; / 30.4.7.16.8 TransactionOverhead &lt;TxOvrhd&gt; / 30.4.7.16.8.5 IndividualFee &lt;IndvFee&gt; / 30.4.7.16.8.5.1 Type &lt;Tp&gt; / 30.4.7.16.8.5.1.2 Proprietary &lt;Prtry&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00534.md) | 732–732 |
| [30 sese.007.001.10 TransferInConfirmationV10 / 30.4 Message Building Blocks / 30.4.4 RelatedReference &lt;RltdRef&gt; / 30.4.7.16 UnitsDetails &lt;UnitsDtls&gt; / 30.4.7.16.8 TransactionOverhead &lt;TxOvrhd&gt; / 30.4.7.16.8.5 IndividualFee &lt;IndvFee&gt; / 30.4.7.16.8.5.2 Basis &lt;Bsis&gt; / 30.4.7.16.8.5.2.2 Proprietary &lt;Prtry&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00535.md) | 733–733 |
| [30 sese.007.001.10 TransferInConfirmationV10 / 30.4 Message Building Blocks / 30.4.4 RelatedReference &lt;RltdRef&gt; / 30.4.7.16 UnitsDetails &lt;UnitsDtls&gt; / 30.4.7.16.8 TransactionOverhead &lt;TxOvrhd&gt; / 30.4.7.16.8.5 IndividualFee &lt;IndvFee&gt; / 30.4.7.16.8.5.5 DiscountDetails &lt;DscntDtls&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00536.md) | 734–734 |
| [30 sese.007.001.10 TransferInConfirmationV10 / 30.4 Message Building Blocks / 30.4.4 RelatedReference &lt;RltdRef&gt; / 30.4.7.16 UnitsDetails &lt;UnitsDtls&gt; / 30.4.7.16.8 TransactionOverhead &lt;TxOvrhd&gt; / 30.4.7.16.8.5 IndividualFee &lt;IndvFee&gt; / 30.4.7.16.8.5.5 DiscountDetails &lt;DscntDtls&gt; / 30.4.7.16.8.5.5.2 Rate &lt;Rate&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00537.md) | 735–735 |
| [30 sese.007.001.10 TransferInConfirmationV10 / 30.4 Message Building Blocks / 30.4.4 RelatedReference &lt;RltdRef&gt; / 30.4.7.16 UnitsDetails &lt;UnitsDtls&gt; / 30.4.7.16.8 TransactionOverhead &lt;TxOvrhd&gt; / 30.4.7.16.8.5 IndividualFee &lt;IndvFee&gt; / 30.4.7.16.8.5.6 AppliedAmount &lt;ApldAmt&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00538.md) | 736–736 |
| [30 sese.007.001.10 TransferInConfirmationV10 / 30.4 Message Building Blocks / 30.4.4 RelatedReference &lt;RltdRef&gt; / 30.4.7.16 UnitsDetails &lt;UnitsDtls&gt; / 30.4.7.16.8 TransactionOverhead &lt;TxOvrhd&gt; / 30.4.7.16.8.5 IndividualFee &lt;IndvFee&gt; / 30.4.7.16.8.5.10 InformativeIndicator &lt;InftvInd&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00539.md) | 737–737 |
| [30 sese.007.001.10 TransferInConfirmationV10 / 30.4 Message Building Blocks / 30.4.4 RelatedReference &lt;RltdRef&gt; / 30.4.7.16 UnitsDetails &lt;UnitsDtls&gt; / 30.4.7.16.8 TransactionOverhead &lt;TxOvrhd&gt; / 30.4.7.16.8.7 DigitalNetworkFee &lt;DgtlNtwkFee&gt; / 30.4.7.16.8.7.1 FinancialInstrumentIdentification &lt;FinInstrmId&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00540.md) | 738–739 |
| [30 sese.007.001.10 TransferInConfirmationV10 / 30.4 Message Building Blocks / 30.4.4 RelatedReference &lt;RltdRef&gt; / 30.4.7.16 UnitsDetails &lt;UnitsDtls&gt; / 30.4.7.16.8 TransactionOverhead &lt;TxOvrhd&gt; / 30.4.7.16.8.7 DigitalNetworkFee &lt;DgtlNtwkFee&gt; / 30.4.7.16.8.7.1 FinancialInstrumentIdentification &lt;FinInstrmId&gt; / 30.4.7.16.8.7.1.1 ISIN &lt;ISIN&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00541.md) | 740–740 |
| [30 sese.007.001.10 TransferInConfirmationV10 / 30.4 Message Building Blocks / 30.4.4 RelatedReference &lt;RltdRef&gt; / 30.4.7.16 UnitsDetails &lt;UnitsDtls&gt; / 30.4.7.16.8 TransactionOverhead &lt;TxOvrhd&gt; / 30.4.7.16.8.7 DigitalNetworkFee &lt;DgtlNtwkFee&gt; / 30.4.7.16.8.7.1 FinancialInstrumentIdentification &lt;FinInstrmId&gt; / 30.4.7.16.8.7.1.2 OtherIdentification &lt;OthrId&gt; / 30.4.7.16.8.7.1.2.3 Type &lt;Tp&gt; / 30.4.7.16.8.7.1.2.3.1 Code &lt;Cd&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00542.md) | 741–741 |
| [30 sese.007.001.10 TransferInConfirmationV10 / 30.4 Message Building Blocks / 30.4.4 RelatedReference &lt;RltdRef&gt; / 30.4.7.16 UnitsDetails &lt;UnitsDtls&gt; / 30.4.7.16.8 TransactionOverhead &lt;TxOvrhd&gt; / 30.4.7.16.8.7 DigitalNetworkFee &lt;DgtlNtwkFee&gt; / 30.4.7.16.8.7.1 FinancialInstrumentIdentification &lt;FinInstrmId&gt; / 30.4.7.16.8.7.1.2 OtherIdentification &lt;OthrId&gt; / 30.4.7.16.8.7.1.2.3 Type &lt;Tp&gt; / 30.4.7.16.8.7.1.2.3.2 Proprietary &lt;Prtry&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00543.md) | 742–742 |
| [30 sese.007.001.10 TransferInConfirmationV10 / 30.4 Message Building Blocks / 30.4.4 RelatedReference &lt;RltdRef&gt; / 30.4.7.16 UnitsDetails &lt;UnitsDtls&gt; / 30.4.7.16.8 TransactionOverhead &lt;TxOvrhd&gt; / 30.4.7.16.8.7 DigitalNetworkFee &lt;DgtlNtwkFee&gt; / 30.4.7.16.8.7.2 Quantity &lt;Qty&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00544.md) | 743–743 |
| [30 sese.007.001.10 TransferInConfirmationV10 / 30.4 Message Building Blocks / 30.4.4 RelatedReference &lt;RltdRef&gt; / 30.4.7.16 UnitsDetails &lt;UnitsDtls&gt; / 30.4.7.16.8 TransactionOverhead &lt;TxOvrhd&gt; / 30.4.7.16.8.7 DigitalNetworkFee &lt;DgtlNtwkFee&gt; / 30.4.7.16.8.7.2 Quantity &lt;Qty&gt; / 30.4.7.16.8.7.2.2 ProprietaryQuantity &lt;PrtryQty&gt; / 30.4.7.16.8.7.2.2.1 Quantity &lt;Qty&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00545.md) | 744–744 |
| [30 sese.007.001.10 TransferInConfirmationV10 / 30.4 Message Building Blocks / 30.4.4 RelatedReference &lt;RltdRef&gt; / 30.4.7.16 UnitsDetails &lt;UnitsDtls&gt; / 30.4.7.16.9 OtherAmount &lt;OthrAmt&gt; / 30.4.7.16.9.1 Type &lt;Tp&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00546.md) | 745–745 |
| [30 sese.007.001.10 TransferInConfirmationV10 / 30.4 Message Building Blocks / 30.4.4 RelatedReference &lt;RltdRef&gt; / 30.4.7.17 Rounding &lt;Rndg&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00547.md) | 746–746 |
| [30 sese.007.001.10 TransferInConfirmationV10 / 30.4 Message Building Blocks / 30.4.4 RelatedReference &lt;RltdRef&gt; / 30.4.7.20 NewAveragePrice &lt;NewAvrgPric&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00548.md) | 747–747 |
| [30 sese.007.001.10 TransferInConfirmationV10 / 30.4 Message Building Blocks / 30.4.4 RelatedReference &lt;RltdRef&gt; / 30.4.7.24 OwnAccountTransferIndicator &lt;OwnAcctTrfInd&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00549.md) | 748–748 |
| [30 sese.007.001.10 TransferInConfirmationV10 / 30.4 Message Building Blocks / 30.4.8 AccountDetails &lt;AcctDtls&gt; / 30.4.8.1 OwnerIdentification &lt;OwnrId&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00550.md) | 749–749 |
| [30 sese.007.001.10 TransferInConfirmationV10 / 30.4 Message Building Blocks / 30.4.8 AccountDetails &lt;AcctDtls&gt; / 30.4.8.2 AccountIdentification &lt;AcctId&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00551.md) | 750–750 |
| [30 sese.007.001.10 TransferInConfirmationV10 / 30.4 Message Building Blocks / 30.4.8 AccountDetails &lt;AcctDtls&gt; / 30.4.8.7 BlockChainAddressOrWallet &lt;BlckChainAdrOrWllt&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00552.md) | 751–751 |
| [30 sese.007.001.10 TransferInConfirmationV10 / 30.4 Message Building Blocks / 30.4.8 AccountDetails &lt;AcctDtls&gt; / 30.4.8.10 DematerialisedIndicator &lt;DmtrlsdInd&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00553.md) | 752–752 |
| [30 sese.007.001.10 TransferInConfirmationV10 / 30.4 Message Building Blocks / 30.4.8 AccountDetails &lt;AcctDtls&gt; / 30.4.8.14 SettlementPartiesDetails &lt;SttlmPtiesDtls&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00554.md) | 753–753 |
| [30 sese.007.001.10 TransferInConfirmationV10 / 30.4 Message Building Blocks / 30.4.8 AccountDetails &lt;AcctDtls&gt; / 30.4.8.14 SettlementPartiesDetails &lt;SttlmPtiesDtls&gt; / 30.4.8.14.2 SettlementTransactionCondition &lt;SttlmTxCond&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00555.md) | 754–755 |
| [30 sese.007.001.10 TransferInConfirmationV10 / 30.4 Message Building Blocks / 30.4.8 AccountDetails &lt;AcctDtls&gt; / 30.4.8.14 SettlementPartiesDetails &lt;SttlmPtiesDtls&gt; / 30.4.8.14.4 ReceivingSideDetails &lt;RcvgSdDtls&gt; / 30.4.8.14.4.1 Depository &lt;Dpstry&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00556.md) | 756–756 |
| [30 sese.007.001.10 TransferInConfirmationV10 / 30.4 Message Building Blocks / 30.4.8 AccountDetails &lt;AcctDtls&gt; / 30.4.8.14 SettlementPartiesDetails &lt;SttlmPtiesDtls&gt; / 30.4.8.14.4 ReceivingSideDetails &lt;RcvgSdDtls&gt; / 30.4.8.14.4.2 Party1 &lt;Pty1&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00557.md) | 757–757 |
| [30 sese.007.001.10 TransferInConfirmationV10 / 30.4 Message Building Blocks / 30.4.8 AccountDetails &lt;AcctDtls&gt; / 30.4.8.14 SettlementPartiesDetails &lt;SttlmPtiesDtls&gt; / 30.4.8.14.4 ReceivingSideDetails &lt;RcvgSdDtls&gt; / 30.4.8.14.4.5 Party4 &lt;Pty4&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00558.md) | 758–760 |
| [30 sese.007.001.10 TransferInConfirmationV10 / 30.4 Message Building Blocks / 30.4.8 AccountDetails &lt;AcctDtls&gt; / 30.4.9.1 Transferor &lt;Trfr&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00559.md) | 761–761 |
| [30 sese.007.001.10 TransferInConfirmationV10 / 30.4 Message Building Blocks / 30.4.8 AccountDetails &lt;AcctDtls&gt; / 30.4.9.2 TransferorRegisteredAccount &lt;TrfrRegdAcct&gt; / 30.4.9.2.1 Identification &lt;Id&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00560.md) | 762–762 |
| [30 sese.007.001.10 TransferInConfirmationV10 / 30.4 Message Building Blocks / 30.4.8 AccountDetails &lt;AcctDtls&gt; / 30.4.9.2 TransferorRegisteredAccount &lt;TrfrRegdAcct&gt; / 30.4.9.2.6 BlockChainAddressOrWallet &lt;BlckChainAdrOrWllt&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00561.md) | 763–763 |
| [30 sese.007.001.10 TransferInConfirmationV10 / 30.4 Message Building Blocks / 30.4.8 AccountDetails &lt;AcctDtls&gt; / 30.4.9.5 DematerialisedIndicator &lt;DmtrlsdInd&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00562.md) | 764–764 |
| [30 sese.007.001.10 TransferInConfirmationV10 / 30.4 Message Building Blocks / 30.4.8 AccountDetails &lt;AcctDtls&gt; / 30.4.9.9 RequestedSettlementDate &lt;ReqdSttlmDt&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00563.md) | 765–765 |
| [30 sese.007.001.10 TransferInConfirmationV10 / 30.4 Message Building Blocks / 30.4.8 AccountDetails &lt;AcctDtls&gt; / 30.4.9.13 NetAmount &lt;NetAmt&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00564.md) | 766–766 |
| [30 sese.007.001.10 TransferInConfirmationV10 / 30.4 Message Building Blocks / 30.4.8 AccountDetails &lt;AcctDtls&gt; / 30.4.9.15 IndividualTax &lt;IndvTax&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00565.md) | 767–767 |
| [30 sese.007.001.10 TransferInConfirmationV10 / 30.4 Message Building Blocks / 30.4.8 AccountDetails &lt;AcctDtls&gt; / 30.4.9.16 ForeignExchangeDetails &lt;FXDtls&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00566.md) | 768–768 |
| [30 sese.007.001.10 TransferInConfirmationV10 / 30.4 Message Building Blocks / 30.4.8 AccountDetails &lt;AcctDtls&gt; / 30.4.9.17 SettlementPartiesDetails &lt;SttlmPtiesDtls&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00567.md) | 769–769 |
| [30 sese.007.001.10 TransferInConfirmationV10 / 30.4 Message Building Blocks / 30.4.8 AccountDetails &lt;AcctDtls&gt; / 30.4.9.17 SettlementPartiesDetails &lt;SttlmPtiesDtls&gt; / 30.4.9.17.1 TradeTransactionCondition &lt;TradTxCond&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00568.md) | 770–771 |
| [30 sese.007.001.10 TransferInConfirmationV10 / 30.4 Message Building Blocks / 30.4.8 AccountDetails &lt;AcctDtls&gt; / 30.4.9.17 SettlementPartiesDetails &lt;SttlmPtiesDtls&gt; / 30.4.9.17.4 DeliveringSideDetails &lt;DlvrgSdDtls&gt; / 30.4.9.17.4.1 Depository &lt;Dpstry&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00569.md) | 772–772 |
| [30 sese.007.001.10 TransferInConfirmationV10 / 30.4 Message Building Blocks / 30.4.8 AccountDetails &lt;AcctDtls&gt; / 30.4.9.17 SettlementPartiesDetails &lt;SttlmPtiesDtls&gt; / 30.4.9.17.4 DeliveringSideDetails &lt;DlvrgSdDtls&gt; / 30.4.9.17.4.2 Party1 &lt;Pty1&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00570.md) | 773–773 |
| [30 sese.007.001.10 TransferInConfirmationV10 / 30.4 Message Building Blocks / 30.4.8 AccountDetails &lt;AcctDtls&gt; / 30.4.9.17 SettlementPartiesDetails &lt;SttlmPtiesDtls&gt; / 30.4.9.17.4 DeliveringSideDetails &lt;DlvrgSdDtls&gt; / 30.4.9.17.4.5 Party4 &lt;Pty4&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00571.md) | 774–774 |
| [30 sese.007.001.10 TransferInConfirmationV10 / 30.4 Message Building Blocks / 30.4.8 AccountDetails &lt;AcctDtls&gt; / 30.4.9.18 PhysicalTransfer &lt;PhysTrf&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00572.md) | 775–775 |
| [30 sese.007.001.10 TransferInConfirmationV10 / 30.4 Message Building Blocks / 30.4.8 AccountDetails &lt;AcctDtls&gt; / 30.4.9.20 ClientReference &lt;ClntRef&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00573.md) | 776–777 |

## Scoped participants and related business flows

| Reference | Kind | Source |
| --- | --- | --- |
| [Beneficial Owner](../../../../../shared/reference/participants/participant-src-000095-beneficial-owner.md) | participant | src-000095 |
| [Concentrator](../../../../../shared/reference/participants/participant-src-000095-concentrator.md) | participant | src-000095 |
| [CSD / ICSD](../../../../../shared/reference/participants/participant-src-000095-csd-icsd.md) | participant | src-000095 |
| [CSD](../../../../../shared/reference/participants/participant-src-000095-csd.md) | participant | src-000095 |
| [Custodian](../../../../../shared/reference/participants/participant-src-000095-custodian.md) | participant | src-000095 |
| [Distributor](../../../../../shared/reference/participants/participant-src-000095-distributor.md) | participant | src-000095 |
| [Executing Party / Registering Party](../../../../../shared/reference/participants/participant-src-000095-executing-party-registering-party.md) | participant | src-000095 |
| [Executing Party](../../../../../shared/reference/participants/participant-src-000095-executing-party.md) | participant | src-000095 |
| [Fund Accountant](../../../../../shared/reference/participants/participant-src-000095-fund-accountant.md) | participant | src-000095 |
| [Fund Manager](../../../../../shared/reference/participants/participant-src-000095-fund-manager.md) | participant | src-000095 |
| [ICSD](../../../../../shared/reference/participants/participant-src-000095-icsd.md) | participant | src-000095 |
| [Institutional Investor](../../../../../shared/reference/participants/participant-src-000095-institutional-investor.md) | participant | src-000095 |
| [Instructing Party](../../../../../shared/reference/participants/participant-src-000095-instructing-party.md) | participant | src-000095 |
| [Intermediary](../../../../../shared/reference/participants/participant-src-000095-intermediary.md) | participant | src-000095 |
| [Market Data Provider](../../../../../shared/reference/participants/participant-src-000095-market-data-provider.md) | participant | src-000095 |
| [Paying Agent](../../../../../shared/reference/participants/participant-src-000095-paying-agent.md) | participant | src-000095 |
| [Receiving Party (all levels)](../../../../../shared/reference/participants/participant-src-000095-receiving-party-all-levels.md) | participant | src-000095 |
| [Reporting Party](../../../../../shared/reference/participants/participant-src-000095-reporting-party.md) | participant | src-000095 |
| [Requesting Party](../../../../../shared/reference/participants/participant-src-000095-requesting-party.md) | participant | src-000095 |
| [Transfer Agent](../../../../../shared/reference/participants/participant-src-000095-transfer-agent.md) | participant | src-000095 |
| [Transferee's Bank (Executing Party)](../../../../../shared/reference/participants/participant-src-000095-transferee-s-bank-executing-party.md) | participant | src-000095 |
| [Transferee's Bank (Instructing Party)](../../../../../shared/reference/participants/participant-src-000095-transferee-s-bank-instructing-party.md) | participant | src-000095 |
| [Transferee](../../../../../shared/reference/participants/participant-src-000095-transferee.md) | participant | src-000095 |
| [Transferor's Bank (Executing Party)](../../../../../shared/reference/participants/participant-src-000095-transferor-s-bank-executing-party.md) | participant | src-000095 |
| [Transferor's Bank (Instructing Party)](../../../../../shared/reference/participants/participant-src-000095-transferor-s-bank-instructing-party.md) | participant | src-000095 |
| [Transferor](../../../../../shared/reference/participants/participant-src-000095-transferor.md) | participant | src-000095 |
| [Account Administration](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p185-account-administration.md) | business-flow | src-000095 |
| [Order Processing](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p186-order-processing.md) | business-flow | src-000095 |
| [Order Execution](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p187-order-execution.md) | business-flow | src-000095 |
| [Payment Execution](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p188-payment-execution.md) | business-flow | src-000095 |
| [Payment Execution - Advance Pay In](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p189-payment-execution-advance-pay-in.md) | business-flow | src-000095 |
| [Payment Execution - Pay In Arrears](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p190-payment-execution-pay-in-arrears.md) | business-flow | src-000095 |
| [Payment Execution - Pay Out Arrears](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p191-payment-execution-pay-out-arrears.md) | business-flow | src-000095 |
| [Tax Accounting](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p192-tax-accounting.md) | business-flow | src-000095 |
| [Fund Valuation](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p193-fund-valuation.md) | business-flow | src-000095 |
| [Commission Accounting](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p194-commission-accounting.md) | business-flow | src-000095 |
| [Commission Accounting / Transaction Based Commission Accounting](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p195-commission-accounting-transaction-based-commission-accounting.md) | business-flow | src-000095 |
| [Commission Accounting / Trailer Commission Accounting](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p196-commission-accounting-trailer-commission-accounting.md) | business-flow | src-000095 |
| [Reconciliation](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p197-reconciliation.md) | business-flow | src-000095 |
| [Distribution](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p199-distribution.md) | business-flow | src-000095 |
| [Registration](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p200-registration.md) | business-flow | src-000095 |
| [Account Opening](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p205-account-opening.md) | business-flow | src-000095 |
| [Account Modification](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p207-account-modification.md) | business-flow | src-000095 |
| [Reporting](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p209-reporting.md) | business-flow | src-000095 |
| [Order Processing](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p212-order-processing.md) | business-flow | src-000095 |
| [Custody and Accounting](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p216-custody-and-accounting.md) | business-flow | src-000095 |
| [Transparency of Holdings](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p218-transparency-of-holdings.md) | business-flow | src-000095 |
| [Stock Transfers (Single Leg Transfer)](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p221-stock-transfers-single-leg-transfer.md) | business-flow | src-000095 |
| [Portfolio and Stock Transfers (Single Leg)](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p226-portfolio-and-stock-transfers-single-leg.md) | business-flow | src-000095 |
| [Portfolio and Stock Transfers (Double/Matched Leg)](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p230-portfolio-and-stock-transfers-double-matched-leg.md) | business-flow | src-000095 |

[Canonical message](index.md) · [Schema structure](structure.md) · [Known gaps](../../../../../tracking/issues.md)
