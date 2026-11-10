---
template: false
document_kind: "message-mdr-evidence"
review_status: "needs-review"
domain: "securities"
message_id: "sese.005.001.10"
message_family: "sese.005"
namespace: "urn:iso:std:iso:20022:tech:xsd:sese.005.001.10"
source_ids: ["src-000096"]
source_locations: [{"source_id": "src-000096", "heading": "28 sese.005.001.10 TransferInInstructionV10", "file_pages": [608, 688]}]
limitations: ["PDF text and candidate tables require visual reconciliation; business-role mapping is not inferred from XML names.", "Separate publication statements are retained without version-comparison or silent conflict resolution."]
source_editions: ["May 2026"]
---

# sese.005.001.10 MDR business evidence

The following supplied publications explicitly define this exact message identifier. Functionality text is retained with page locators; detailed definitions, rules, tables and figures remain in focused source sections. This page does not substitute one message version for another.

## src-000096 — 28 sese.005.001.10 TransferInInstructionV10

[src-000096](../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md); file pp608–688; publication May 2026. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000096, 28 sese.005.001.10 TransferInInstructionV10, Functionality, file p608.**

The TransferInInstruction message is sent by an instructing party, for example, an investment manager
or its authorised representative, to the executing party, for example, a transfer agent, to instruct the
receipt of a financial instrument, free of payment, on a given date from a specified party.
This message may also be used to instruct the receipt of a financial instrument, free of payment, from
another of the instructing parties own accounts or from a third party.
Usage
The TransferInInstruction message is used to instruct the receipt of a financial instrument from another
account, either owned by the instructing party or by a third party.
Outline
The TransferInInstructionV10 MessageDefinition is composed of 12 MessageBuildingBlocks:
A. MessageIdentification
Reference that uniquely identifies the message from a business application standpoint.
B. PoolReference
Collective reference identifying a set of messages.
C. PreviousReference
Reference to a linked message that was previously sent.
D. RelatedReference
Reference to a linked message that was previously received.
E. Function
Function of the transfer in, that is, whether the transfer in message is used as an instruction or an
advice and request for information. The absence of Function indicates the message is an
instruction.
F. MasterReference
Unique and unambiguous identifier for a group of individual transfers as assigned by the instructing
party. This identifier links the individual transfers together.
G. TransferDetails
General information related to the transfer of the financial instrument.
H. AccountDetails
Information related to the account into which the financial instrument is to be received.
I. SettlementDetails
Information related to the delivering side of the transfer.
J. MarketPracticeVersion
Approved by the Securities SEG on 27 January 2026 sese.005.001.10 TransferInInstructionV10
Investment Funds - Maintenance 2025 - 2026 608 May 2026

**src-000096, 28 sese.005.001.10 TransferInInstructionV10, Functionality, file p609.**

Identifies the market practice to which the message conforms.
K. CopyDetails
Information provided when the message is a copy of a previous message.
L. Extension
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities SEG on 27 January 2026 sese.005.001.10 TransferInInstructionV10
Investment Funds - Maintenance 2025 - 2026 609 May 2026

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/investment-funds/2025-2026/documents/src-000096/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [27 sese.004.001.09 ReversalOfTransferOutConfirmationV09 / 28.1 MessageDefinition Functionality](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00447.md) | 608–609 |
| [27 sese.004.001.09 ReversalOfTransferOutConfirmationV09 / 28.2 Structure](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00448.md) | 610–615 |
| [27 sese.004.001.09 ReversalOfTransferOutConfirmationV09 / 28.3 Constraints](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00449.md) | 616–618 |
| [27 sese.004.001.09 ReversalOfTransferOutConfirmationV09 / 28.4 Message Building Blocks](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00450.md) | 619–619 |
| [27 sese.004.001.09 ReversalOfTransferOutConfirmationV09 / 28.4 Message Building Blocks / 28.4.5 Function &lt;Fctn&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00451.md) | 620–624 |
| [27 sese.004.001.09 ReversalOfTransferOutConfirmationV09 / 28.4 Message Building Blocks / 28.4.6 MasterReference &lt;MstrRef&gt; / 28.4.7.1 TransferReference &lt;TrfRef&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00452.md) | 625–625 |
| [27 sese.004.001.09 ReversalOfTransferOutConfirmationV09 / 28.4 Message Building Blocks / 28.4.6 MasterReference &lt;MstrRef&gt; / 28.4.7.3 CounterpartyReference &lt;CtrPtyRef&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00453.md) | 626–626 |
| [27 sese.004.001.09 ReversalOfTransferOutConfirmationV09 / 28.4 Message Building Blocks / 28.4.6 MasterReference &lt;MstrRef&gt; / 28.4.7.6 RequestedSettlementDate &lt;ReqdSttlmDt&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00454.md) | 627–627 |
| [27 sese.004.001.09 ReversalOfTransferOutConfirmationV09 / 28.4 Message Building Blocks / 28.4.6 MasterReference &lt;MstrRef&gt; / 28.4.7.10 FinancialInstrumentDetails &lt;FinInstrmDtls&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00455.md) | 628–628 |
| [27 sese.004.001.09 ReversalOfTransferOutConfirmationV09 / 28.4 Message Building Blocks / 28.4.6 MasterReference &lt;MstrRef&gt; / 28.4.7.10 FinancialInstrumentDetails &lt;FinInstrmDtls&gt; / 28.4.7.10.1 Identification &lt;Id&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00456.md) | 629–629 |
| [27 sese.004.001.09 ReversalOfTransferOutConfirmationV09 / 28.4 Message Building Blocks / 28.4.6 MasterReference &lt;MstrRef&gt; / 28.4.7.10 FinancialInstrumentDetails &lt;FinInstrmDtls&gt; / 28.4.7.10.1 Identification &lt;Id&gt; / 28.4.7.10.1.2 SEDOL &lt;SEDOL&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00457.md) | 630–630 |
| [27 sese.004.001.09 ReversalOfTransferOutConfirmationV09 / 28.4 Message Building Blocks / 28.4.6 MasterReference &lt;MstrRef&gt; / 28.4.7.10 FinancialInstrumentDetails &lt;FinInstrmDtls&gt; / 28.4.7.10.1 Identification &lt;Id&gt; / 28.4.7.10.1.9 Wertpapier &lt;Wrtppr&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00458.md) | 631–631 |
| [27 sese.004.001.09 ReversalOfTransferOutConfirmationV09 / 28.4 Message Building Blocks / 28.4.6 MasterReference &lt;MstrRef&gt; / 28.4.7.10 FinancialInstrumentDetails &lt;FinInstrmDtls&gt; / 28.4.7.10.1 Identification &lt;Id&gt; / 28.4.7.10.1.16 OtherProprietaryIdentification &lt;OthrPrtryId&gt; / 28.4.7.10.1.16.1 Identification &lt;Id&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00459.md) | 632–632 |
| [27 sese.004.001.09 ReversalOfTransferOutConfirmationV09 / 28.4 Message Building Blocks / 28.4.6 MasterReference &lt;MstrRef&gt; / 28.4.7.10 FinancialInstrumentDetails &lt;FinInstrmDtls&gt; / 28.4.7.10.6 SecuritiesForm &lt;SctiesForm&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00460.md) | 633–633 |
| [27 sese.004.001.09 ReversalOfTransferOutConfirmationV09 / 28.4 Message Building Blocks / 28.4.6 MasterReference &lt;MstrRef&gt; / 28.4.7.11 Quantity &lt;Qty&gt; / 28.4.7.11.1 TotalUnitsNumber &lt;TtlUnitsNb&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00461.md) | 634–636 |
| [27 sese.004.001.09 ReversalOfTransferOutConfirmationV09 / 28.4 Message Building Blocks / 28.4.6 MasterReference &lt;MstrRef&gt; / 28.4.7.12 UnitsDetails &lt;UnitsDtls&gt; / 28.4.7.12.1 Units &lt;Units&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00462.md) | 637–637 |
| [27 sese.004.001.09 ReversalOfTransferOutConfirmationV09 / 28.4 Message Building Blocks / 28.4.6 MasterReference &lt;MstrRef&gt; / 28.4.7.12 UnitsDetails &lt;UnitsDtls&gt; / 28.4.7.12.6 Reference &lt;Ref&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00463.md) | 638–639 |
| [27 sese.004.001.09 ReversalOfTransferOutConfirmationV09 / 28.4 Message Building Blocks / 28.4.6 MasterReference &lt;MstrRef&gt; / 28.4.7.12 UnitsDetails &lt;UnitsDtls&gt; / 28.4.7.12.8 TransactionOverhead &lt;TxOvrhd&gt; / 28.4.7.12.8.1 TotalOverheadApplied &lt;TtlOvrhdApld&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00464.md) | 640–640 |
| [27 sese.004.001.09 ReversalOfTransferOutConfirmationV09 / 28.4 Message Building Blocks / 28.4.6 MasterReference &lt;MstrRef&gt; / 28.4.7.12 UnitsDetails &lt;UnitsDtls&gt; / 28.4.7.12.8 TransactionOverhead &lt;TxOvrhd&gt; / 28.4.7.12.8.2 TotalFees &lt;TtlFees&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00465.md) | 641–641 |
| [27 sese.004.001.09 ReversalOfTransferOutConfirmationV09 / 28.4 Message Building Blocks / 28.4.6 MasterReference &lt;MstrRef&gt; / 28.4.7.12 UnitsDetails &lt;UnitsDtls&gt; / 28.4.7.12.8 TransactionOverhead &lt;TxOvrhd&gt; / 28.4.7.12.8.5 IndividualFee &lt;IndvFee&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00466.md) | 642–642 |
| [27 sese.004.001.09 ReversalOfTransferOutConfirmationV09 / 28.4 Message Building Blocks / 28.4.6 MasterReference &lt;MstrRef&gt; / 28.4.7.12 UnitsDetails &lt;UnitsDtls&gt; / 28.4.7.12.8 TransactionOverhead &lt;TxOvrhd&gt; / 28.4.7.12.8.5 IndividualFee &lt;IndvFee&gt; / 28.4.7.12.8.5.1 Type &lt;Tp&gt; / 28.4.7.12.8.5.1.1 Code &lt;Cd&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00467.md) | 643–643 |
| [27 sese.004.001.09 ReversalOfTransferOutConfirmationV09 / 28.4 Message Building Blocks / 28.4.6 MasterReference &lt;MstrRef&gt; / 28.4.7.12 UnitsDetails &lt;UnitsDtls&gt; / 28.4.7.12.8 TransactionOverhead &lt;TxOvrhd&gt; / 28.4.7.12.8.5 IndividualFee &lt;IndvFee&gt; / 28.4.7.12.8.5.1 Type &lt;Tp&gt; / 28.4.7.12.8.5.1.2 Proprietary &lt;Prtry&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00468.md) | 644–644 |
| [27 sese.004.001.09 ReversalOfTransferOutConfirmationV09 / 28.4 Message Building Blocks / 28.4.6 MasterReference &lt;MstrRef&gt; / 28.4.7.12 UnitsDetails &lt;UnitsDtls&gt; / 28.4.7.12.8 TransactionOverhead &lt;TxOvrhd&gt; / 28.4.7.12.8.5 IndividualFee &lt;IndvFee&gt; / 28.4.7.12.8.5.2 Basis &lt;Bsis&gt; / 28.4.7.12.8.5.2.2 Proprietary &lt;Prtry&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00469.md) | 645–645 |
| [27 sese.004.001.09 ReversalOfTransferOutConfirmationV09 / 28.4 Message Building Blocks / 28.4.6 MasterReference &lt;MstrRef&gt; / 28.4.7.12 UnitsDetails &lt;UnitsDtls&gt; / 28.4.7.12.8 TransactionOverhead &lt;TxOvrhd&gt; / 28.4.7.12.8.5 IndividualFee &lt;IndvFee&gt; / 28.4.7.12.8.5.5 DiscountDetails &lt;DscntDtls&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00470.md) | 646–646 |
| [27 sese.004.001.09 ReversalOfTransferOutConfirmationV09 / 28.4 Message Building Blocks / 28.4.6 MasterReference &lt;MstrRef&gt; / 28.4.7.12 UnitsDetails &lt;UnitsDtls&gt; / 28.4.7.12.8 TransactionOverhead &lt;TxOvrhd&gt; / 28.4.7.12.8.5 IndividualFee &lt;IndvFee&gt; / 28.4.7.12.8.5.5 DiscountDetails &lt;DscntDtls&gt; / 28.4.7.12.8.5.5.2 Rate &lt;Rate&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00471.md) | 647–647 |
| [27 sese.004.001.09 ReversalOfTransferOutConfirmationV09 / 28.4 Message Building Blocks / 28.4.6 MasterReference &lt;MstrRef&gt; / 28.4.7.12 UnitsDetails &lt;UnitsDtls&gt; / 28.4.7.12.8 TransactionOverhead &lt;TxOvrhd&gt; / 28.4.7.12.8.5 IndividualFee &lt;IndvFee&gt; / 28.4.7.12.8.5.6 AppliedAmount &lt;ApldAmt&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00472.md) | 648–648 |
| [27 sese.004.001.09 ReversalOfTransferOutConfirmationV09 / 28.4 Message Building Blocks / 28.4.6 MasterReference &lt;MstrRef&gt; / 28.4.7.12 UnitsDetails &lt;UnitsDtls&gt; / 28.4.7.12.8 TransactionOverhead &lt;TxOvrhd&gt; / 28.4.7.12.8.5 IndividualFee &lt;IndvFee&gt; / 28.4.7.12.8.5.10 InformativeIndicator &lt;InftvInd&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00473.md) | 649–649 |
| [27 sese.004.001.09 ReversalOfTransferOutConfirmationV09 / 28.4 Message Building Blocks / 28.4.6 MasterReference &lt;MstrRef&gt; / 28.4.7.12 UnitsDetails &lt;UnitsDtls&gt; / 28.4.7.12.8 TransactionOverhead &lt;TxOvrhd&gt; / 28.4.7.12.8.7 DigitalNetworkFee &lt;DgtlNtwkFee&gt; / 28.4.7.12.8.7.1 FinancialInstrumentIdentification &lt;FinInstrmId&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00474.md) | 650–651 |
| [27 sese.004.001.09 ReversalOfTransferOutConfirmationV09 / 28.4 Message Building Blocks / 28.4.6 MasterReference &lt;MstrRef&gt; / 28.4.7.12 UnitsDetails &lt;UnitsDtls&gt; / 28.4.7.12.8 TransactionOverhead &lt;TxOvrhd&gt; / 28.4.7.12.8.7 DigitalNetworkFee &lt;DgtlNtwkFee&gt; / 28.4.7.12.8.7.1 FinancialInstrumentIdentification &lt;FinInstrmId&gt; / 28.4.7.12.8.7.1.1 ISIN &lt;ISIN&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00475.md) | 652–652 |
| [27 sese.004.001.09 ReversalOfTransferOutConfirmationV09 / 28.4 Message Building Blocks / 28.4.6 MasterReference &lt;MstrRef&gt; / 28.4.7.12 UnitsDetails &lt;UnitsDtls&gt; / 28.4.7.12.8 TransactionOverhead &lt;TxOvrhd&gt; / 28.4.7.12.8.7 DigitalNetworkFee &lt;DgtlNtwkFee&gt; / 28.4.7.12.8.7.1 FinancialInstrumentIdentification &lt;FinInstrmId&gt; / 28.4.7.12.8.7.1.2 OtherIdentification &lt;OthrId&gt; / 28.4.7.12.8.7.1.2.3 Type &lt;Tp&gt; / 28.4.7.12.8.7.1.2.3.1 Code &lt;Cd&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00476.md) | 653–653 |
| [27 sese.004.001.09 ReversalOfTransferOutConfirmationV09 / 28.4 Message Building Blocks / 28.4.6 MasterReference &lt;MstrRef&gt; / 28.4.7.12 UnitsDetails &lt;UnitsDtls&gt; / 28.4.7.12.8 TransactionOverhead &lt;TxOvrhd&gt; / 28.4.7.12.8.7 DigitalNetworkFee &lt;DgtlNtwkFee&gt; / 28.4.7.12.8.7.1 FinancialInstrumentIdentification &lt;FinInstrmId&gt; / 28.4.7.12.8.7.1.2 OtherIdentification &lt;OthrId&gt; / 28.4.7.12.8.7.1.2.3 Type &lt;Tp&gt; / 28.4.7.12.8.7.1.2.3.2 Proprietary &lt;Prtry&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00477.md) | 654–654 |
| [27 sese.004.001.09 ReversalOfTransferOutConfirmationV09 / 28.4 Message Building Blocks / 28.4.6 MasterReference &lt;MstrRef&gt; / 28.4.7.12 UnitsDetails &lt;UnitsDtls&gt; / 28.4.7.12.8 TransactionOverhead &lt;TxOvrhd&gt; / 28.4.7.12.8.7 DigitalNetworkFee &lt;DgtlNtwkFee&gt; / 28.4.7.12.8.7.2 Quantity &lt;Qty&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00478.md) | 655–655 |
| [27 sese.004.001.09 ReversalOfTransferOutConfirmationV09 / 28.4 Message Building Blocks / 28.4.6 MasterReference &lt;MstrRef&gt; / 28.4.7.12 UnitsDetails &lt;UnitsDtls&gt; / 28.4.7.12.8 TransactionOverhead &lt;TxOvrhd&gt; / 28.4.7.12.8.7 DigitalNetworkFee &lt;DgtlNtwkFee&gt; / 28.4.7.12.8.7.2 Quantity &lt;Qty&gt; / 28.4.7.12.8.7.2.2 ProprietaryQuantity &lt;PrtryQty&gt; / 28.4.7.12.8.7.2.2.1 Quantity &lt;Qty&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00479.md) | 656–656 |
| [27 sese.004.001.09 ReversalOfTransferOutConfirmationV09 / 28.4 Message Building Blocks / 28.4.6 MasterReference &lt;MstrRef&gt; / 28.4.7.12 UnitsDetails &lt;UnitsDtls&gt; / 28.4.7.12.9 OtherAmount &lt;OthrAmt&gt; / 28.4.7.12.9.1 Type &lt;Tp&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00480.md) | 657–657 |
| [27 sese.004.001.09 ReversalOfTransferOutConfirmationV09 / 28.4 Message Building Blocks / 28.4.6 MasterReference &lt;MstrRef&gt; / 28.4.7.13 Rounding &lt;Rndg&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00481.md) | 658–658 |
| [27 sese.004.001.09 ReversalOfTransferOutConfirmationV09 / 28.4 Message Building Blocks / 28.4.6 MasterReference &lt;MstrRef&gt; / 28.4.7.16 TransferCurrency &lt;TrfCcy&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00482.md) | 659–660 |
| [27 sese.004.001.09 ReversalOfTransferOutConfirmationV09 / 28.4 Message Building Blocks / 28.4.6 MasterReference &lt;MstrRef&gt; / 28.4.8.1 OwnerIdentification &lt;OwnrId&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00483.md) | 661–661 |
| [27 sese.004.001.09 ReversalOfTransferOutConfirmationV09 / 28.4 Message Building Blocks / 28.4.6 MasterReference &lt;MstrRef&gt; / 28.4.8.2 AccountIdentification &lt;AcctId&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00484.md) | 662–662 |
| [27 sese.004.001.09 ReversalOfTransferOutConfirmationV09 / 28.4 Message Building Blocks / 28.4.6 MasterReference &lt;MstrRef&gt; / 28.4.8.7 BlockChainAddressOrWallet &lt;BlckChainAdrOrWllt&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00485.md) | 663–663 |
| [27 sese.004.001.09 ReversalOfTransferOutConfirmationV09 / 28.4 Message Building Blocks / 28.4.6 MasterReference &lt;MstrRef&gt; / 28.4.8.10 DematerialisedIndicator &lt;DmtrlsdInd&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00486.md) | 664–664 |
| [27 sese.004.001.09 ReversalOfTransferOutConfirmationV09 / 28.4 Message Building Blocks / 28.4.6 MasterReference &lt;MstrRef&gt; / 28.4.8.14 SettlementPartiesDetails &lt;SttlmPtiesDtls&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00487.md) | 665–665 |
| [27 sese.004.001.09 ReversalOfTransferOutConfirmationV09 / 28.4 Message Building Blocks / 28.4.6 MasterReference &lt;MstrRef&gt; / 28.4.8.14 SettlementPartiesDetails &lt;SttlmPtiesDtls&gt; / 28.4.8.14.2 SettlementTransactionCondition &lt;SttlmTxCond&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00488.md) | 666–667 |
| [27 sese.004.001.09 ReversalOfTransferOutConfirmationV09 / 28.4 Message Building Blocks / 28.4.6 MasterReference &lt;MstrRef&gt; / 28.4.8.14 SettlementPartiesDetails &lt;SttlmPtiesDtls&gt; / 28.4.8.14.4 ReceivingSideDetails &lt;RcvgSdDtls&gt; / 28.4.8.14.4.1 Depository &lt;Dpstry&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00489.md) | 668–668 |
| [27 sese.004.001.09 ReversalOfTransferOutConfirmationV09 / 28.4 Message Building Blocks / 28.4.6 MasterReference &lt;MstrRef&gt; / 28.4.8.14 SettlementPartiesDetails &lt;SttlmPtiesDtls&gt; / 28.4.8.14.4 ReceivingSideDetails &lt;RcvgSdDtls&gt; / 28.4.8.14.4.2 Party1 &lt;Pty1&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00490.md) | 669–669 |
| [27 sese.004.001.09 ReversalOfTransferOutConfirmationV09 / 28.4 Message Building Blocks / 28.4.6 MasterReference &lt;MstrRef&gt; / 28.4.8.14 SettlementPartiesDetails &lt;SttlmPtiesDtls&gt; / 28.4.8.14.4 ReceivingSideDetails &lt;RcvgSdDtls&gt; / 28.4.8.14.4.5 Party4 &lt;Pty4&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00491.md) | 670–672 |
| [27 sese.004.001.09 ReversalOfTransferOutConfirmationV09 / 28.4 Message Building Blocks / 28.4.6 MasterReference &lt;MstrRef&gt; / 28.4.9.1 Transferor &lt;Trfr&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00492.md) | 673–673 |
| [27 sese.004.001.09 ReversalOfTransferOutConfirmationV09 / 28.4 Message Building Blocks / 28.4.6 MasterReference &lt;MstrRef&gt; / 28.4.9.2 TransferorRegisteredAccount &lt;TrfrRegdAcct&gt; / 28.4.9.2.1 Identification &lt;Id&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00493.md) | 674–674 |
| [27 sese.004.001.09 ReversalOfTransferOutConfirmationV09 / 28.4 Message Building Blocks / 28.4.6 MasterReference &lt;MstrRef&gt; / 28.4.9.2 TransferorRegisteredAccount &lt;TrfrRegdAcct&gt; / 28.4.9.2.6 BlockChainAddressOrWallet &lt;BlckChainAdrOrWllt&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00494.md) | 675–675 |
| [27 sese.004.001.09 ReversalOfTransferOutConfirmationV09 / 28.4 Message Building Blocks / 28.4.6 MasterReference &lt;MstrRef&gt; / 28.4.9.5 DematerialisedIndicator &lt;DmtrlsdInd&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00495.md) | 676–676 |
| [27 sese.004.001.09 ReversalOfTransferOutConfirmationV09 / 28.4 Message Building Blocks / 28.4.6 MasterReference &lt;MstrRef&gt; / 28.4.9.9 RequestedSettlementDate &lt;ReqdSttlmDt&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00496.md) | 677–677 |
| [27 sese.004.001.09 ReversalOfTransferOutConfirmationV09 / 28.4 Message Building Blocks / 28.4.6 MasterReference &lt;MstrRef&gt; / 28.4.9.13 Fees &lt;Fees&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00497.md) | 678–678 |
| [27 sese.004.001.09 ReversalOfTransferOutConfirmationV09 / 28.4 Message Building Blocks / 28.4.6 MasterReference &lt;MstrRef&gt; / 28.4.9.14 IndividualTax &lt;IndvTax&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00498.md) | 679–679 |
| [27 sese.004.001.09 ReversalOfTransferOutConfirmationV09 / 28.4 Message Building Blocks / 28.4.6 MasterReference &lt;MstrRef&gt; / 28.4.9.16 SettlementPartiesDetails &lt;SttlmPtiesDtls&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00499.md) | 680–680 |
| [27 sese.004.001.09 ReversalOfTransferOutConfirmationV09 / 28.4 Message Building Blocks / 28.4.6 MasterReference &lt;MstrRef&gt; / 28.4.9.16 SettlementPartiesDetails &lt;SttlmPtiesDtls&gt; / 28.4.9.16.1 TradeTransactionCondition &lt;TradTxCond&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00500.md) | 681–681 |
| [27 sese.004.001.09 ReversalOfTransferOutConfirmationV09 / 28.4 Message Building Blocks / 28.4.6 MasterReference &lt;MstrRef&gt; / 28.4.9.16 SettlementPartiesDetails &lt;SttlmPtiesDtls&gt; / 28.4.9.16.3 SecuritiesSettlementSystemIdentification &lt;SctiesSttlmSysId&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00501.md) | 682–682 |
| [27 sese.004.001.09 ReversalOfTransferOutConfirmationV09 / 28.4 Message Building Blocks / 28.4.6 MasterReference &lt;MstrRef&gt; / 28.4.9.16 SettlementPartiesDetails &lt;SttlmPtiesDtls&gt; / 28.4.9.16.4 DeliveringSideDetails &lt;DlvrgSdDtls&gt; / 28.4.9.16.4.1 Depository &lt;Dpstry&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00502.md) | 683–683 |
| [27 sese.004.001.09 ReversalOfTransferOutConfirmationV09 / 28.4 Message Building Blocks / 28.4.6 MasterReference &lt;MstrRef&gt; / 28.4.9.16 SettlementPartiesDetails &lt;SttlmPtiesDtls&gt; / 28.4.9.16.4 DeliveringSideDetails &lt;DlvrgSdDtls&gt; / 28.4.9.16.4.2 Party1 &lt;Pty1&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00503.md) | 684–684 |
| [27 sese.004.001.09 ReversalOfTransferOutConfirmationV09 / 28.4 Message Building Blocks / 28.4.6 MasterReference &lt;MstrRef&gt; / 28.4.9.16 SettlementPartiesDetails &lt;SttlmPtiesDtls&gt; / 28.4.9.16.4 DeliveringSideDetails &lt;DlvrgSdDtls&gt; / 28.4.9.16.4.4 Party3 &lt;Pty3&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00504.md) | 685–685 |
| [27 sese.004.001.09 ReversalOfTransferOutConfirmationV09 / 28.4 Message Building Blocks / 28.4.6 MasterReference &lt;MstrRef&gt; / 28.4.9.16 SettlementPartiesDetails &lt;SttlmPtiesDtls&gt; / 28.4.9.16.4 DeliveringSideDetails &lt;DlvrgSdDtls&gt; / 28.4.9.16.4.6 Party5 &lt;Pty5&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00505.md) | 686–686 |
| [27 sese.004.001.09 ReversalOfTransferOutConfirmationV09 / 28.4 Message Building Blocks / 28.4.6 MasterReference &lt;MstrRef&gt; / 28.4.9.19 ClientReference &lt;ClntRef&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00506.md) | 687–688 |

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
