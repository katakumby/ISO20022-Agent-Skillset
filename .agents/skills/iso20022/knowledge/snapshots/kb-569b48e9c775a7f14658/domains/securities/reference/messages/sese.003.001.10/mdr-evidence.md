---
template: false
document_kind: "message-mdr-evidence"
review_status: "needs-review"
domain: "securities"
message_id: "sese.003.001.10"
message_family: "sese.003"
namespace: "urn:iso:std:iso:20022:tech:xsd:sese.003.001.10"
source_ids: ["src-000096"]
source_locations: [{"source_id": "src-000096", "heading": "26 sese.003.001.10 TransferOutConfirmationV10", "file_pages": [519, 601]}]
limitations: ["PDF text and candidate tables require visual reconciliation; business-role mapping is not inferred from XML names.", "Separate publication statements are retained without version-comparison or silent conflict resolution."]
source_editions: ["May 2026"]
---

# sese.003.001.10 MDR business evidence

The following supplied publications explicitly define this exact message identifier. Functionality text is retained with page locators; detailed definitions, rules, tables and figures remain in focused source sections. This page does not substitute one message version for another.

## src-000096 — 26 sese.003.001.10 TransferOutConfirmationV10

[src-000096](../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md); file pp519–601; publication May 2026. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000096, 26 sese.003.001.10 TransferOutConfirmationV10, Functionality, file p519.**

The TransferOutConfirmation message is sent by an executing party, for example, a transfer agent, to
the instructing party, for example, an investment manager or its authorised representative, to confirm
the delivery of a financial instrument, free of payment, on a given date, to a specified party.
This message may also be used to confirm the delivery of a financial instrument, free of payment, to
another of the instructing parties own accounts or to a third party.
Usage
The TransferOutConfirmation message is used to confirm the withdrawal of a financial instrument from
the owner's account and its delivery to another own account, or to a third party, has taken place.
The reference of the transfer confirmation is identified in TransferConfirmationReference. The reference
of the original transfer instruction is specified in TransferReference. The message identification of the
TransferOutInstruction message in which the transfer instruction was conveyed may also be quoted in
RelatedReference but this is not recommended.
Outline
The TransferOutConfirmationV10 MessageDefinition is composed of 11 MessageBuildingBlocks:
A. MessageIdentification
Reference that uniquely identifies the message from a business application standpoint.
B. PoolReference
Collective reference identifying a set of messages.
C. PreviousReference
Reference to a linked message that was previously sent.
D. RelatedReference
Reference to a linked message that was previously received.
E. MasterReference
Unique and unambiguous identifier for a group of individual transfers as assigned by the instructing
party. This identifier links the individual transfers together.
F. TransferDetails
General information related to the transfer of the financial instrument.
G. AccountDetails
Information related to the account from which the financial instrument was withdrawn.
H. SettlementDetails
Information related to the receiving side of the transfer.
I. MarketPracticeVersion
Approved by the Securities SEG on 27 January 2026 sese.003.001.10 TransferOutConfirmationV10
Investment Funds - Maintenance 2025 - 2026 519 May 2026

**src-000096, 26 sese.003.001.10 TransferOutConfirmationV10, Functionality, file p520.**

Identifies the market practice to which the message conforms.
J. CopyDetails
Information provided when the message is a copy of a previous message.
K. Extension
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities SEG on 27 January 2026 sese.003.001.10 TransferOutConfirmationV10
Investment Funds - Maintenance 2025 - 2026 520 May 2026

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/investment-funds/2025-2026/documents/src-000096/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [25 sese.002.001.09 TransferOutCancellationRequestV09 / 26.1 MessageDefinition Functionality](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00380.md) | 519–520 |
| [25 sese.002.001.09 TransferOutCancellationRequestV09 / 26.2 Structure](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00381.md) | 521–526 |
| [25 sese.002.001.09 TransferOutCancellationRequestV09 / 26.3 Constraints](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00382.md) | 527–529 |
| [25 sese.002.001.09 TransferOutCancellationRequestV09 / 26.4 Message Building Blocks](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00383.md) | 530–530 |
| [25 sese.002.001.09 TransferOutCancellationRequestV09 / 26.4 Message Building Blocks / 26.4.5 MasterReference &lt;MstrRef&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00384.md) | 531–535 |
| [25 sese.002.001.09 TransferOutCancellationRequestV09 / 26.4 Message Building Blocks / 26.4.6 TransferDetails &lt;TrfDtls&gt; / 26.4.6.1 TransferConfirmationReference &lt;TrfConfRef&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00385.md) | 536–536 |
| [25 sese.002.001.09 TransferOutCancellationRequestV09 / 26.4 Message Building Blocks / 26.4.6 TransferDetails &lt;TrfDtls&gt; / 26.4.6.3 ClientReference &lt;ClntRef&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00386.md) | 537–537 |
| [25 sese.002.001.09 TransferOutCancellationRequestV09 / 26.4 Message Building Blocks / 26.4.6 TransferDetails &lt;TrfDtls&gt; / 26.4.6.6 RequestedSettlementDate &lt;ReqdSttlmDt&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00387.md) | 538–538 |
| [25 sese.002.001.09 TransferOutCancellationRequestV09 / 26.4 Message Building Blocks / 26.4.6 TransferDetails &lt;TrfDtls&gt; / 26.4.6.11 TransferReason &lt;TrfRsn&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00388.md) | 539–540 |
| [25 sese.002.001.09 TransferOutCancellationRequestV09 / 26.4 Message Building Blocks / 26.4.6 TransferDetails &lt;TrfDtls&gt; / 26.4.6.13 FinancialInstrumentDetails &lt;FinInstrmDtls&gt; / 26.4.6.13.1 Identification &lt;Id&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00389.md) | 541–541 |
| [25 sese.002.001.09 TransferOutCancellationRequestV09 / 26.4 Message Building Blocks / 26.4.6 TransferDetails &lt;TrfDtls&gt; / 26.4.6.13 FinancialInstrumentDetails &lt;FinInstrmDtls&gt; / 26.4.6.13.1 Identification &lt;Id&gt; / 26.4.6.13.1.3 CUSIP &lt;CUSIP&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00390.md) | 542–542 |
| [25 sese.002.001.09 TransferOutCancellationRequestV09 / 26.4 Message Building Blocks / 26.4.6 TransferDetails &lt;TrfDtls&gt; / 26.4.6.13 FinancialInstrumentDetails &lt;FinInstrmDtls&gt; / 26.4.6.13.1 Identification &lt;Id&gt; / 26.4.6.13.1.10 Dutch &lt;Dtch&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00391.md) | 543–543 |
| [25 sese.002.001.09 TransferOutCancellationRequestV09 / 26.4 Message Building Blocks / 26.4.6 TransferDetails &lt;TrfDtls&gt; / 26.4.6.13 FinancialInstrumentDetails &lt;FinInstrmDtls&gt; / 26.4.6.13.1 Identification &lt;Id&gt; / 26.4.6.13.1.16 OtherProprietaryIdentification &lt;OthrPrtryId&gt; / 26.4.6.13.1.16.1 Identification &lt;Id&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00392.md) | 544–544 |
| [25 sese.002.001.09 TransferOutCancellationRequestV09 / 26.4 Message Building Blocks / 26.4.6 TransferDetails &lt;TrfDtls&gt; / 26.4.6.13 FinancialInstrumentDetails &lt;FinInstrmDtls&gt; / 26.4.6.13.6 SecuritiesForm &lt;SctiesForm&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00393.md) | 545–545 |
| [25 sese.002.001.09 TransferOutCancellationRequestV09 / 26.4 Message Building Blocks / 26.4.6 TransferDetails &lt;TrfDtls&gt; / 26.4.6.14 TotalUnitsNumber &lt;TtlUnitsNb&gt; / 26.4.6.14.1 UnitsNumber &lt;UnitsNb&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00394.md) | 546–548 |
| [25 sese.002.001.09 TransferOutCancellationRequestV09 / 26.4 Message Building Blocks / 26.4.6 TransferDetails &lt;TrfDtls&gt; / 26.4.6.16 UnitsDetails &lt;UnitsDtls&gt; / 26.4.6.16.1 Units &lt;Units&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00395.md) | 549–549 |
| [25 sese.002.001.09 TransferOutCancellationRequestV09 / 26.4 Message Building Blocks / 26.4.6 TransferDetails &lt;TrfDtls&gt; / 26.4.6.16 UnitsDetails &lt;UnitsDtls&gt; / 26.4.6.16.6 Reference &lt;Ref&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00396.md) | 550–551 |
| [25 sese.002.001.09 TransferOutCancellationRequestV09 / 26.4 Message Building Blocks / 26.4.6 TransferDetails &lt;TrfDtls&gt; / 26.4.6.16 UnitsDetails &lt;UnitsDtls&gt; / 26.4.6.16.8 TransactionOverhead &lt;TxOvrhd&gt; / 26.4.6.16.8.1 TotalOverheadApplied &lt;TtlOvrhdApld&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00397.md) | 552–552 |
| [25 sese.002.001.09 TransferOutCancellationRequestV09 / 26.4 Message Building Blocks / 26.4.6 TransferDetails &lt;TrfDtls&gt; / 26.4.6.16 UnitsDetails &lt;UnitsDtls&gt; / 26.4.6.16.8 TransactionOverhead &lt;TxOvrhd&gt; / 26.4.6.16.8.2 TotalFees &lt;TtlFees&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00398.md) | 553–553 |
| [25 sese.002.001.09 TransferOutCancellationRequestV09 / 26.4 Message Building Blocks / 26.4.6 TransferDetails &lt;TrfDtls&gt; / 26.4.6.16 UnitsDetails &lt;UnitsDtls&gt; / 26.4.6.16.8 TransactionOverhead &lt;TxOvrhd&gt; / 26.4.6.16.8.5 IndividualFee &lt;IndvFee&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00399.md) | 554–554 |
| [25 sese.002.001.09 TransferOutCancellationRequestV09 / 26.4 Message Building Blocks / 26.4.6 TransferDetails &lt;TrfDtls&gt; / 26.4.6.16 UnitsDetails &lt;UnitsDtls&gt; / 26.4.6.16.8 TransactionOverhead &lt;TxOvrhd&gt; / 26.4.6.16.8.5 IndividualFee &lt;IndvFee&gt; / 26.4.6.16.8.5.1 Type &lt;Tp&gt; / 26.4.6.16.8.5.1.1 Code &lt;Cd&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00400.md) | 555–555 |
| [25 sese.002.001.09 TransferOutCancellationRequestV09 / 26.4 Message Building Blocks / 26.4.6 TransferDetails &lt;TrfDtls&gt; / 26.4.6.16 UnitsDetails &lt;UnitsDtls&gt; / 26.4.6.16.8 TransactionOverhead &lt;TxOvrhd&gt; / 26.4.6.16.8.5 IndividualFee &lt;IndvFee&gt; / 26.4.6.16.8.5.1 Type &lt;Tp&gt; / 26.4.6.16.8.5.1.2 Proprietary &lt;Prtry&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00401.md) | 556–556 |
| [25 sese.002.001.09 TransferOutCancellationRequestV09 / 26.4 Message Building Blocks / 26.4.6 TransferDetails &lt;TrfDtls&gt; / 26.4.6.16 UnitsDetails &lt;UnitsDtls&gt; / 26.4.6.16.8 TransactionOverhead &lt;TxOvrhd&gt; / 26.4.6.16.8.5 IndividualFee &lt;IndvFee&gt; / 26.4.6.16.8.5.2 Basis &lt;Bsis&gt; / 26.4.6.16.8.5.2.2 Proprietary &lt;Prtry&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00402.md) | 557–557 |
| [25 sese.002.001.09 TransferOutCancellationRequestV09 / 26.4 Message Building Blocks / 26.4.6 TransferDetails &lt;TrfDtls&gt; / 26.4.6.16 UnitsDetails &lt;UnitsDtls&gt; / 26.4.6.16.8 TransactionOverhead &lt;TxOvrhd&gt; / 26.4.6.16.8.5 IndividualFee &lt;IndvFee&gt; / 26.4.6.16.8.5.5 DiscountDetails &lt;DscntDtls&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00403.md) | 558–558 |
| [25 sese.002.001.09 TransferOutCancellationRequestV09 / 26.4 Message Building Blocks / 26.4.6 TransferDetails &lt;TrfDtls&gt; / 26.4.6.16 UnitsDetails &lt;UnitsDtls&gt; / 26.4.6.16.8 TransactionOverhead &lt;TxOvrhd&gt; / 26.4.6.16.8.5 IndividualFee &lt;IndvFee&gt; / 26.4.6.16.8.5.5 DiscountDetails &lt;DscntDtls&gt; / 26.4.6.16.8.5.5.2 Rate &lt;Rate&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00404.md) | 559–559 |
| [25 sese.002.001.09 TransferOutCancellationRequestV09 / 26.4 Message Building Blocks / 26.4.6 TransferDetails &lt;TrfDtls&gt; / 26.4.6.16 UnitsDetails &lt;UnitsDtls&gt; / 26.4.6.16.8 TransactionOverhead &lt;TxOvrhd&gt; / 26.4.6.16.8.5 IndividualFee &lt;IndvFee&gt; / 26.4.6.16.8.5.6 AppliedAmount &lt;ApldAmt&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00405.md) | 560–560 |
| [25 sese.002.001.09 TransferOutCancellationRequestV09 / 26.4 Message Building Blocks / 26.4.6 TransferDetails &lt;TrfDtls&gt; / 26.4.6.16 UnitsDetails &lt;UnitsDtls&gt; / 26.4.6.16.8 TransactionOverhead &lt;TxOvrhd&gt; / 26.4.6.16.8.5 IndividualFee &lt;IndvFee&gt; / 26.4.6.16.8.5.10 InformativeIndicator &lt;InftvInd&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00406.md) | 561–561 |
| [25 sese.002.001.09 TransferOutCancellationRequestV09 / 26.4 Message Building Blocks / 26.4.6 TransferDetails &lt;TrfDtls&gt; / 26.4.6.16 UnitsDetails &lt;UnitsDtls&gt; / 26.4.6.16.8 TransactionOverhead &lt;TxOvrhd&gt; / 26.4.6.16.8.7 DigitalNetworkFee &lt;DgtlNtwkFee&gt; / 26.4.6.16.8.7.1 FinancialInstrumentIdentification &lt;FinInstrmId&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00407.md) | 562–563 |
| [25 sese.002.001.09 TransferOutCancellationRequestV09 / 26.4 Message Building Blocks / 26.4.6 TransferDetails &lt;TrfDtls&gt; / 26.4.6.16 UnitsDetails &lt;UnitsDtls&gt; / 26.4.6.16.8 TransactionOverhead &lt;TxOvrhd&gt; / 26.4.6.16.8.7 DigitalNetworkFee &lt;DgtlNtwkFee&gt; / 26.4.6.16.8.7.1 FinancialInstrumentIdentification &lt;FinInstrmId&gt; / 26.4.6.16.8.7.1.1 ISIN &lt;ISIN&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00408.md) | 564–564 |
| [25 sese.002.001.09 TransferOutCancellationRequestV09 / 26.4 Message Building Blocks / 26.4.6 TransferDetails &lt;TrfDtls&gt; / 26.4.6.16 UnitsDetails &lt;UnitsDtls&gt; / 26.4.6.16.8 TransactionOverhead &lt;TxOvrhd&gt; / 26.4.6.16.8.7 DigitalNetworkFee &lt;DgtlNtwkFee&gt; / 26.4.6.16.8.7.1 FinancialInstrumentIdentification &lt;FinInstrmId&gt; / 26.4.6.16.8.7.1.2 OtherIdentification &lt;OthrId&gt; / 26.4.6.16.8.7.1.2.3 Type &lt;Tp&gt; / 26.4.6.16.8.7.1.2.3.1 Code &lt;Cd&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00409.md) | 565–565 |
| [25 sese.002.001.09 TransferOutCancellationRequestV09 / 26.4 Message Building Blocks / 26.4.6 TransferDetails &lt;TrfDtls&gt; / 26.4.6.16 UnitsDetails &lt;UnitsDtls&gt; / 26.4.6.16.8 TransactionOverhead &lt;TxOvrhd&gt; / 26.4.6.16.8.7 DigitalNetworkFee &lt;DgtlNtwkFee&gt; / 26.4.6.16.8.7.1 FinancialInstrumentIdentification &lt;FinInstrmId&gt; / 26.4.6.16.8.7.1.2 OtherIdentification &lt;OthrId&gt; / 26.4.6.16.8.7.1.2.3 Type &lt;Tp&gt; / 26.4.6.16.8.7.1.2.3.2 Proprietary &lt;Prtry&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00410.md) | 566–566 |
| [25 sese.002.001.09 TransferOutCancellationRequestV09 / 26.4 Message Building Blocks / 26.4.6 TransferDetails &lt;TrfDtls&gt; / 26.4.6.16 UnitsDetails &lt;UnitsDtls&gt; / 26.4.6.16.8 TransactionOverhead &lt;TxOvrhd&gt; / 26.4.6.16.8.7 DigitalNetworkFee &lt;DgtlNtwkFee&gt; / 26.4.6.16.8.7.2 Quantity &lt;Qty&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00411.md) | 567–567 |
| [25 sese.002.001.09 TransferOutCancellationRequestV09 / 26.4 Message Building Blocks / 26.4.6 TransferDetails &lt;TrfDtls&gt; / 26.4.6.16 UnitsDetails &lt;UnitsDtls&gt; / 26.4.6.16.8 TransactionOverhead &lt;TxOvrhd&gt; / 26.4.6.16.8.7 DigitalNetworkFee &lt;DgtlNtwkFee&gt; / 26.4.6.16.8.7.2 Quantity &lt;Qty&gt; / 26.4.6.16.8.7.2.2 ProprietaryQuantity &lt;PrtryQty&gt; / 26.4.6.16.8.7.2.2.1 Quantity &lt;Qty&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00412.md) | 568–568 |
| [25 sese.002.001.09 TransferOutCancellationRequestV09 / 26.4 Message Building Blocks / 26.4.6 TransferDetails &lt;TrfDtls&gt; / 26.4.6.16 UnitsDetails &lt;UnitsDtls&gt; / 26.4.6.16.9 OtherAmount &lt;OthrAmt&gt; / 26.4.6.16.9.1 Type &lt;Tp&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00413.md) | 569–569 |
| [25 sese.002.001.09 TransferOutCancellationRequestV09 / 26.4 Message Building Blocks / 26.4.6 TransferDetails &lt;TrfDtls&gt; / 26.4.6.17 Rounding &lt;Rndg&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00414.md) | 570–570 |
| [25 sese.002.001.09 TransferOutCancellationRequestV09 / 26.4 Message Building Blocks / 26.4.6 TransferDetails &lt;TrfDtls&gt; / 26.4.6.20 NewAveragePrice &lt;NewAvrgPric&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00415.md) | 571–571 |
| [25 sese.002.001.09 TransferOutCancellationRequestV09 / 26.4 Message Building Blocks / 26.4.6 TransferDetails &lt;TrfDtls&gt; / 26.4.6.24 OwnAccountTransferIndicator &lt;OwnAcctTrfInd&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00416.md) | 572–572 |
| [25 sese.002.001.09 TransferOutCancellationRequestV09 / 26.4 Message Building Blocks / 26.4.6 TransferDetails &lt;TrfDtls&gt; / 26.4.7.1 OwnerIdentification &lt;OwnrId&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00417.md) | 573–573 |
| [25 sese.002.001.09 TransferOutCancellationRequestV09 / 26.4 Message Building Blocks / 26.4.6 TransferDetails &lt;TrfDtls&gt; / 26.4.7.2 AccountIdentification &lt;AcctId&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00418.md) | 574–574 |
| [25 sese.002.001.09 TransferOutCancellationRequestV09 / 26.4 Message Building Blocks / 26.4.6 TransferDetails &lt;TrfDtls&gt; / 26.4.7.7 BlockChainAddressOrWallet &lt;BlckChainAdrOrWllt&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00419.md) | 575–575 |
| [25 sese.002.001.09 TransferOutCancellationRequestV09 / 26.4 Message Building Blocks / 26.4.6 TransferDetails &lt;TrfDtls&gt; / 26.4.7.10 DematerialisedIndicator &lt;DmtrlsdInd&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00420.md) | 576–576 |
| [25 sese.002.001.09 TransferOutCancellationRequestV09 / 26.4 Message Building Blocks / 26.4.6 TransferDetails &lt;TrfDtls&gt; / 26.4.7.14 SettlementPartiesDetails &lt;SttlmPtiesDtls&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00421.md) | 577–577 |
| [25 sese.002.001.09 TransferOutCancellationRequestV09 / 26.4 Message Building Blocks / 26.4.6 TransferDetails &lt;TrfDtls&gt; / 26.4.7.14 SettlementPartiesDetails &lt;SttlmPtiesDtls&gt; / 26.4.7.14.2 SettlementTransactionCondition &lt;SttlmTxCond&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00422.md) | 578–579 |
| [25 sese.002.001.09 TransferOutCancellationRequestV09 / 26.4 Message Building Blocks / 26.4.6 TransferDetails &lt;TrfDtls&gt; / 26.4.7.14 SettlementPartiesDetails &lt;SttlmPtiesDtls&gt; / 26.4.7.14.4 DeliveringSideDetails &lt;DlvrgSdDtls&gt; / 26.4.7.14.4.1 Depository &lt;Dpstry&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00423.md) | 580–580 |
| [25 sese.002.001.09 TransferOutCancellationRequestV09 / 26.4 Message Building Blocks / 26.4.6 TransferDetails &lt;TrfDtls&gt; / 26.4.7.14 SettlementPartiesDetails &lt;SttlmPtiesDtls&gt; / 26.4.7.14.4 DeliveringSideDetails &lt;DlvrgSdDtls&gt; / 26.4.7.14.4.2 Party1 &lt;Pty1&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00424.md) | 581–581 |
| [25 sese.002.001.09 TransferOutCancellationRequestV09 / 26.4 Message Building Blocks / 26.4.6 TransferDetails &lt;TrfDtls&gt; / 26.4.7.14 SettlementPartiesDetails &lt;SttlmPtiesDtls&gt; / 26.4.7.14.4 DeliveringSideDetails &lt;DlvrgSdDtls&gt; / 26.4.7.14.4.5 Party4 &lt;Pty4&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00425.md) | 582–584 |
| [25 sese.002.001.09 TransferOutCancellationRequestV09 / 26.4 Message Building Blocks / 26.4.6 TransferDetails &lt;TrfDtls&gt; / 26.4.8.1 Transferee &lt;Trfee&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00426.md) | 585–585 |
| [25 sese.002.001.09 TransferOutCancellationRequestV09 / 26.4 Message Building Blocks / 26.4.6 TransferDetails &lt;TrfDtls&gt; / 26.4.8.2 TransfereeRegisteredAccount &lt;TrfeeRegdAcct&gt; / 26.4.8.2.1 Identification &lt;Id&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00427.md) | 586–586 |
| [25 sese.002.001.09 TransferOutCancellationRequestV09 / 26.4 Message Building Blocks / 26.4.6 TransferDetails &lt;TrfDtls&gt; / 26.4.8.2 TransfereeRegisteredAccount &lt;TrfeeRegdAcct&gt; / 26.4.8.2.6 BlockChainAddressOrWallet &lt;BlckChainAdrOrWllt&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00428.md) | 587–587 |
| [25 sese.002.001.09 TransferOutCancellationRequestV09 / 26.4 Message Building Blocks / 26.4.6 TransferDetails &lt;TrfDtls&gt; / 26.4.8.5 DematerialisedIndicator &lt;DmtrlsdInd&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00429.md) | 588–588 |
| [25 sese.002.001.09 TransferOutCancellationRequestV09 / 26.4 Message Building Blocks / 26.4.6 TransferDetails &lt;TrfDtls&gt; / 26.4.8.9 RequestedSettlementDate &lt;ReqdSttlmDt&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00430.md) | 589–589 |
| [25 sese.002.001.09 TransferOutCancellationRequestV09 / 26.4 Message Building Blocks / 26.4.6 TransferDetails &lt;TrfDtls&gt; / 26.4.8.13 NetAmount &lt;NetAmt&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00431.md) | 590–590 |
| [25 sese.002.001.09 TransferOutCancellationRequestV09 / 26.4 Message Building Blocks / 26.4.6 TransferDetails &lt;TrfDtls&gt; / 26.4.8.15 IndividualTax &lt;IndvTax&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00432.md) | 591–591 |
| [25 sese.002.001.09 TransferOutCancellationRequestV09 / 26.4 Message Building Blocks / 26.4.6 TransferDetails &lt;TrfDtls&gt; / 26.4.8.16 ForeignExchangeDetails &lt;FXDtls&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00433.md) | 592–592 |
| [25 sese.002.001.09 TransferOutCancellationRequestV09 / 26.4 Message Building Blocks / 26.4.6 TransferDetails &lt;TrfDtls&gt; / 26.4.8.17 SettlementPartiesDetails &lt;SttlmPtiesDtls&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00434.md) | 593–593 |
| [25 sese.002.001.09 TransferOutCancellationRequestV09 / 26.4 Message Building Blocks / 26.4.6 TransferDetails &lt;TrfDtls&gt; / 26.4.8.17 SettlementPartiesDetails &lt;SttlmPtiesDtls&gt; / 26.4.8.17.1 TradeTransactionCondition &lt;TradTxCond&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00435.md) | 594–595 |
| [25 sese.002.001.09 TransferOutCancellationRequestV09 / 26.4 Message Building Blocks / 26.4.6 TransferDetails &lt;TrfDtls&gt; / 26.4.8.17 SettlementPartiesDetails &lt;SttlmPtiesDtls&gt; / 26.4.8.17.4 ReceivingSideDetails &lt;RcvgSdDtls&gt; / 26.4.8.17.4.1 Depository &lt;Dpstry&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00436.md) | 596–596 |
| [25 sese.002.001.09 TransferOutCancellationRequestV09 / 26.4 Message Building Blocks / 26.4.6 TransferDetails &lt;TrfDtls&gt; / 26.4.8.17 SettlementPartiesDetails &lt;SttlmPtiesDtls&gt; / 26.4.8.17.4 ReceivingSideDetails &lt;RcvgSdDtls&gt; / 26.4.8.17.4.2 Party1 &lt;Pty1&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00437.md) | 597–597 |
| [25 sese.002.001.09 TransferOutCancellationRequestV09 / 26.4 Message Building Blocks / 26.4.6 TransferDetails &lt;TrfDtls&gt; / 26.4.8.17 SettlementPartiesDetails &lt;SttlmPtiesDtls&gt; / 26.4.8.17.4 ReceivingSideDetails &lt;RcvgSdDtls&gt; / 26.4.8.17.4.5 Party4 &lt;Pty4&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00438.md) | 598–598 |
| [25 sese.002.001.09 TransferOutCancellationRequestV09 / 26.4 Message Building Blocks / 26.4.6 TransferDetails &lt;TrfDtls&gt; / 26.4.8.18 PhysicalTransfer &lt;PhysTrf&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00439.md) | 599–599 |
| [25 sese.002.001.09 TransferOutCancellationRequestV09 / 26.4 Message Building Blocks / 26.4.6 TransferDetails &lt;TrfDtls&gt; / 26.4.8.20 ClientReference &lt;ClntRef&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00440.md) | 600–601 |

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
