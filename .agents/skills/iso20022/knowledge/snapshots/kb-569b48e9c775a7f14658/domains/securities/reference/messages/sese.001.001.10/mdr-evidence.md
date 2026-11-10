---
template: false
document_kind: "message-mdr-evidence"
review_status: "needs-review"
domain: "securities"
message_id: "sese.001.001.10"
message_family: "sese.001"
namespace: "urn:iso:std:iso:20022:tech:xsd:sese.001.001.10"
source_ids: ["src-000096"]
source_locations: [{"source_id": "src-000096", "heading": "24 sese.001.001.10 TransferOutInstructionV10", "file_pages": [433, 512]}]
limitations: ["PDF text and candidate tables require visual reconciliation; business-role mapping is not inferred from XML names.", "Separate publication statements are retained without version-comparison or silent conflict resolution."]
source_editions: ["May 2026"]
---

# sese.001.001.10 MDR business evidence

The following supplied publications explicitly define this exact message identifier. Functionality text is retained with page locators; detailed definitions, rules, tables and figures remain in focused source sections. This page does not substitute one message version for another.

## src-000096 — 24 sese.001.001.10 TransferOutInstructionV10

[src-000096](../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md); file pp433–512; publication May 2026. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000096, 24 sese.001.001.10 TransferOutInstructionV10, Functionality, file p433.**

Scope
The TransferOutInstruction message is sent by an instructing party, for example, an investment
manager or its authorised representative, to the executing party, for example, a transfer agent, to
instruct the delivery of a financial instrument, free of payment, on a given date from a specified party.
This message may also be used to instruct the delivery of a financial instrument, free of payment, to
another of the instructing parties own accounts or to a third party.
Usage
The TransferOutInstruction message is used to instruct the withdrawal of a financial instrument from
one account and deliver it to either another account or to a third party.
Outline
The TransferOutInstructionV10 MessageDefinition is composed of 11 MessageBuildingBlocks:
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
Information related to the account from which the financial instrument is to be withdrawn.
H. SettlementDetails
Information related to the receiving side of the transfer.
I. MarketPracticeVersion
Identifies the market practice to which the message conforms.
J. CopyDetails
Approved by the Securities SEG on 27 January 2026 sese.001.001.10 TransferOutInstructionV10
Investment Funds - Maintenance 2025 - 2026 433 May 2026

**src-000096, 24 sese.001.001.10 TransferOutInstructionV10, Functionality, file p434.**

Information provided when the message is a copy of a previous message.
K. Extension
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities SEG on 27 January 2026 sese.001.001.10 TransferOutInstructionV10
Investment Funds - Maintenance 2025 - 2026 434 May 2026

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/investment-funds/2025-2026/documents/src-000096/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [24 sese.001.001.10 TransferOutInstructionV10](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00313.md) | 433–434 |
| [24 sese.001.001.10 TransferOutInstructionV10 / 24.2 Structure](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00314.md) | 435–440 |
| [24 sese.001.001.10 TransferOutInstructionV10 / 24.3 Constraints](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00315.md) | 441–443 |
| [24 sese.001.001.10 TransferOutInstructionV10 / 24.4 Message Building Blocks](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00316.md) | 444–444 |
| [24 sese.001.001.10 TransferOutInstructionV10 / 24.4 Message Building Blocks / 24.4.4 RelatedReference &lt;RltdRef&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00317.md) | 445–448 |
| [24 sese.001.001.10 TransferOutInstructionV10 / 24.4 Message Building Blocks / 24.4.5 MasterReference &lt;MstrRef&gt; / 24.4.6.1 TransferReference &lt;TrfRef&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00318.md) | 449–449 |
| [24 sese.001.001.10 TransferOutInstructionV10 / 24.4 Message Building Blocks / 24.4.5 MasterReference &lt;MstrRef&gt; / 24.4.6.3 CounterpartyReference &lt;CtrPtyRef&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00319.md) | 450–450 |
| [24 sese.001.001.10 TransferOutInstructionV10 / 24.4 Message Building Blocks / 24.4.5 MasterReference &lt;MstrRef&gt; / 24.4.6.6 RequestedSettlementDate &lt;ReqdSttlmDt&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00320.md) | 451–451 |
| [24 sese.001.001.10 TransferOutInstructionV10 / 24.4 Message Building Blocks / 24.4.5 MasterReference &lt;MstrRef&gt; / 24.4.6.10 FinancialInstrumentDetails &lt;FinInstrmDtls&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00321.md) | 452–452 |
| [24 sese.001.001.10 TransferOutInstructionV10 / 24.4 Message Building Blocks / 24.4.5 MasterReference &lt;MstrRef&gt; / 24.4.6.10 FinancialInstrumentDetails &lt;FinInstrmDtls&gt; / 24.4.6.10.1 Identification &lt;Id&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00322.md) | 453–453 |
| [24 sese.001.001.10 TransferOutInstructionV10 / 24.4 Message Building Blocks / 24.4.5 MasterReference &lt;MstrRef&gt; / 24.4.6.10 FinancialInstrumentDetails &lt;FinInstrmDtls&gt; / 24.4.6.10.1 Identification &lt;Id&gt; / 24.4.6.10.1.2 SEDOL &lt;SEDOL&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00323.md) | 454–454 |
| [24 sese.001.001.10 TransferOutInstructionV10 / 24.4 Message Building Blocks / 24.4.5 MasterReference &lt;MstrRef&gt; / 24.4.6.10 FinancialInstrumentDetails &lt;FinInstrmDtls&gt; / 24.4.6.10.1 Identification &lt;Id&gt; / 24.4.6.10.1.9 Wertpapier &lt;Wrtppr&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00324.md) | 455–455 |
| [24 sese.001.001.10 TransferOutInstructionV10 / 24.4 Message Building Blocks / 24.4.5 MasterReference &lt;MstrRef&gt; / 24.4.6.10 FinancialInstrumentDetails &lt;FinInstrmDtls&gt; / 24.4.6.10.1 Identification &lt;Id&gt; / 24.4.6.10.1.16 OtherProprietaryIdentification &lt;OthrPrtryId&gt; / 24.4.6.10.1.16.1 Identification &lt;Id&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00325.md) | 456–456 |
| [24 sese.001.001.10 TransferOutInstructionV10 / 24.4 Message Building Blocks / 24.4.5 MasterReference &lt;MstrRef&gt; / 24.4.6.10 FinancialInstrumentDetails &lt;FinInstrmDtls&gt; / 24.4.6.10.6 SecuritiesForm &lt;SctiesForm&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00326.md) | 457–457 |
| [24 sese.001.001.10 TransferOutInstructionV10 / 24.4 Message Building Blocks / 24.4.5 MasterReference &lt;MstrRef&gt; / 24.4.6.11 Quantity &lt;Qty&gt; / 24.4.6.11.1 TotalUnitsNumber &lt;TtlUnitsNb&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00327.md) | 458–460 |
| [24 sese.001.001.10 TransferOutInstructionV10 / 24.4 Message Building Blocks / 24.4.5 MasterReference &lt;MstrRef&gt; / 24.4.6.12 UnitsDetails &lt;UnitsDtls&gt; / 24.4.6.12.1 Units &lt;Units&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00328.md) | 461–461 |
| [24 sese.001.001.10 TransferOutInstructionV10 / 24.4 Message Building Blocks / 24.4.5 MasterReference &lt;MstrRef&gt; / 24.4.6.12 UnitsDetails &lt;UnitsDtls&gt; / 24.4.6.12.6 Reference &lt;Ref&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00329.md) | 462–463 |
| [24 sese.001.001.10 TransferOutInstructionV10 / 24.4 Message Building Blocks / 24.4.5 MasterReference &lt;MstrRef&gt; / 24.4.6.12 UnitsDetails &lt;UnitsDtls&gt; / 24.4.6.12.8 TransactionOverhead &lt;TxOvrhd&gt; / 24.4.6.12.8.1 TotalOverheadApplied &lt;TtlOvrhdApld&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00330.md) | 464–464 |
| [24 sese.001.001.10 TransferOutInstructionV10 / 24.4 Message Building Blocks / 24.4.5 MasterReference &lt;MstrRef&gt; / 24.4.6.12 UnitsDetails &lt;UnitsDtls&gt; / 24.4.6.12.8 TransactionOverhead &lt;TxOvrhd&gt; / 24.4.6.12.8.2 TotalFees &lt;TtlFees&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00331.md) | 465–465 |
| [24 sese.001.001.10 TransferOutInstructionV10 / 24.4 Message Building Blocks / 24.4.5 MasterReference &lt;MstrRef&gt; / 24.4.6.12 UnitsDetails &lt;UnitsDtls&gt; / 24.4.6.12.8 TransactionOverhead &lt;TxOvrhd&gt; / 24.4.6.12.8.5 IndividualFee &lt;IndvFee&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00332.md) | 466–466 |
| [24 sese.001.001.10 TransferOutInstructionV10 / 24.4 Message Building Blocks / 24.4.5 MasterReference &lt;MstrRef&gt; / 24.4.6.12 UnitsDetails &lt;UnitsDtls&gt; / 24.4.6.12.8 TransactionOverhead &lt;TxOvrhd&gt; / 24.4.6.12.8.5 IndividualFee &lt;IndvFee&gt; / 24.4.6.12.8.5.1 Type &lt;Tp&gt; / 24.4.6.12.8.5.1.1 Code &lt;Cd&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00333.md) | 467–467 |
| [24 sese.001.001.10 TransferOutInstructionV10 / 24.4 Message Building Blocks / 24.4.5 MasterReference &lt;MstrRef&gt; / 24.4.6.12 UnitsDetails &lt;UnitsDtls&gt; / 24.4.6.12.8 TransactionOverhead &lt;TxOvrhd&gt; / 24.4.6.12.8.5 IndividualFee &lt;IndvFee&gt; / 24.4.6.12.8.5.1 Type &lt;Tp&gt; / 24.4.6.12.8.5.1.2 Proprietary &lt;Prtry&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00334.md) | 468–468 |
| [24 sese.001.001.10 TransferOutInstructionV10 / 24.4 Message Building Blocks / 24.4.5 MasterReference &lt;MstrRef&gt; / 24.4.6.12 UnitsDetails &lt;UnitsDtls&gt; / 24.4.6.12.8 TransactionOverhead &lt;TxOvrhd&gt; / 24.4.6.12.8.5 IndividualFee &lt;IndvFee&gt; / 24.4.6.12.8.5.2 Basis &lt;Bsis&gt; / 24.4.6.12.8.5.2.2 Proprietary &lt;Prtry&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00335.md) | 469–469 |
| [24 sese.001.001.10 TransferOutInstructionV10 / 24.4 Message Building Blocks / 24.4.5 MasterReference &lt;MstrRef&gt; / 24.4.6.12 UnitsDetails &lt;UnitsDtls&gt; / 24.4.6.12.8 TransactionOverhead &lt;TxOvrhd&gt; / 24.4.6.12.8.5 IndividualFee &lt;IndvFee&gt; / 24.4.6.12.8.5.5 DiscountDetails &lt;DscntDtls&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00336.md) | 470–470 |
| [24 sese.001.001.10 TransferOutInstructionV10 / 24.4 Message Building Blocks / 24.4.5 MasterReference &lt;MstrRef&gt; / 24.4.6.12 UnitsDetails &lt;UnitsDtls&gt; / 24.4.6.12.8 TransactionOverhead &lt;TxOvrhd&gt; / 24.4.6.12.8.5 IndividualFee &lt;IndvFee&gt; / 24.4.6.12.8.5.5 DiscountDetails &lt;DscntDtls&gt; / 24.4.6.12.8.5.5.2 Rate &lt;Rate&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00337.md) | 471–471 |
| [24 sese.001.001.10 TransferOutInstructionV10 / 24.4 Message Building Blocks / 24.4.5 MasterReference &lt;MstrRef&gt; / 24.4.6.12 UnitsDetails &lt;UnitsDtls&gt; / 24.4.6.12.8 TransactionOverhead &lt;TxOvrhd&gt; / 24.4.6.12.8.5 IndividualFee &lt;IndvFee&gt; / 24.4.6.12.8.5.6 AppliedAmount &lt;ApldAmt&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00338.md) | 472–472 |
| [24 sese.001.001.10 TransferOutInstructionV10 / 24.4 Message Building Blocks / 24.4.5 MasterReference &lt;MstrRef&gt; / 24.4.6.12 UnitsDetails &lt;UnitsDtls&gt; / 24.4.6.12.8 TransactionOverhead &lt;TxOvrhd&gt; / 24.4.6.12.8.5 IndividualFee &lt;IndvFee&gt; / 24.4.6.12.8.5.10 InformativeIndicator &lt;InftvInd&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00339.md) | 473–473 |
| [24 sese.001.001.10 TransferOutInstructionV10 / 24.4 Message Building Blocks / 24.4.5 MasterReference &lt;MstrRef&gt; / 24.4.6.12 UnitsDetails &lt;UnitsDtls&gt; / 24.4.6.12.8 TransactionOverhead &lt;TxOvrhd&gt; / 24.4.6.12.8.7 DigitalNetworkFee &lt;DgtlNtwkFee&gt; / 24.4.6.12.8.7.1 FinancialInstrumentIdentification &lt;FinInstrmId&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00340.md) | 474–475 |
| [24 sese.001.001.10 TransferOutInstructionV10 / 24.4 Message Building Blocks / 24.4.5 MasterReference &lt;MstrRef&gt; / 24.4.6.12 UnitsDetails &lt;UnitsDtls&gt; / 24.4.6.12.8 TransactionOverhead &lt;TxOvrhd&gt; / 24.4.6.12.8.7 DigitalNetworkFee &lt;DgtlNtwkFee&gt; / 24.4.6.12.8.7.1 FinancialInstrumentIdentification &lt;FinInstrmId&gt; / 24.4.6.12.8.7.1.1 ISIN &lt;ISIN&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00341.md) | 476–476 |
| [24 sese.001.001.10 TransferOutInstructionV10 / 24.4 Message Building Blocks / 24.4.5 MasterReference &lt;MstrRef&gt; / 24.4.6.12 UnitsDetails &lt;UnitsDtls&gt; / 24.4.6.12.8 TransactionOverhead &lt;TxOvrhd&gt; / 24.4.6.12.8.7 DigitalNetworkFee &lt;DgtlNtwkFee&gt; / 24.4.6.12.8.7.1 FinancialInstrumentIdentification &lt;FinInstrmId&gt; / 24.4.6.12.8.7.1.2 OtherIdentification &lt;OthrId&gt; / 24.4.6.12.8.7.1.2.3 Type &lt;Tp&gt; / 24.4.6.12.8.7.1.2.3.1 Code &lt;Cd&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00342.md) | 477–477 |
| [24 sese.001.001.10 TransferOutInstructionV10 / 24.4 Message Building Blocks / 24.4.5 MasterReference &lt;MstrRef&gt; / 24.4.6.12 UnitsDetails &lt;UnitsDtls&gt; / 24.4.6.12.8 TransactionOverhead &lt;TxOvrhd&gt; / 24.4.6.12.8.7 DigitalNetworkFee &lt;DgtlNtwkFee&gt; / 24.4.6.12.8.7.1 FinancialInstrumentIdentification &lt;FinInstrmId&gt; / 24.4.6.12.8.7.1.2 OtherIdentification &lt;OthrId&gt; / 24.4.6.12.8.7.1.2.3 Type &lt;Tp&gt; / 24.4.6.12.8.7.1.2.3.2 Proprietary &lt;Prtry&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00343.md) | 478–478 |
| [24 sese.001.001.10 TransferOutInstructionV10 / 24.4 Message Building Blocks / 24.4.5 MasterReference &lt;MstrRef&gt; / 24.4.6.12 UnitsDetails &lt;UnitsDtls&gt; / 24.4.6.12.8 TransactionOverhead &lt;TxOvrhd&gt; / 24.4.6.12.8.7 DigitalNetworkFee &lt;DgtlNtwkFee&gt; / 24.4.6.12.8.7.2 Quantity &lt;Qty&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00344.md) | 479–479 |
| [24 sese.001.001.10 TransferOutInstructionV10 / 24.4 Message Building Blocks / 24.4.5 MasterReference &lt;MstrRef&gt; / 24.4.6.12 UnitsDetails &lt;UnitsDtls&gt; / 24.4.6.12.8 TransactionOverhead &lt;TxOvrhd&gt; / 24.4.6.12.8.7 DigitalNetworkFee &lt;DgtlNtwkFee&gt; / 24.4.6.12.8.7.2 Quantity &lt;Qty&gt; / 24.4.6.12.8.7.2.2 ProprietaryQuantity &lt;PrtryQty&gt; / 24.4.6.12.8.7.2.2.1 Quantity &lt;Qty&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00345.md) | 480–480 |
| [24 sese.001.001.10 TransferOutInstructionV10 / 24.4 Message Building Blocks / 24.4.5 MasterReference &lt;MstrRef&gt; / 24.4.6.12 UnitsDetails &lt;UnitsDtls&gt; / 24.4.6.12.9 OtherAmount &lt;OthrAmt&gt; / 24.4.6.12.9.1 Type &lt;Tp&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00346.md) | 481–481 |
| [24 sese.001.001.10 TransferOutInstructionV10 / 24.4 Message Building Blocks / 24.4.5 MasterReference &lt;MstrRef&gt; / 24.4.6.13 Rounding &lt;Rndg&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00347.md) | 482–482 |
| [24 sese.001.001.10 TransferOutInstructionV10 / 24.4 Message Building Blocks / 24.4.5 MasterReference &lt;MstrRef&gt; / 24.4.6.16 TransferCurrency &lt;TrfCcy&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00348.md) | 483–483 |
| [24 sese.001.001.10 TransferOutInstructionV10 / 24.4 Message Building Blocks / 24.4.7 AccountDetails &lt;AcctDtls&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00349.md) | 484–484 |
| [24 sese.001.001.10 TransferOutInstructionV10 / 24.4 Message Building Blocks / 24.4.7 AccountDetails &lt;AcctDtls&gt; / 24.4.7.1 OwnerIdentification &lt;OwnrId&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00350.md) | 485–485 |
| [24 sese.001.001.10 TransferOutInstructionV10 / 24.4 Message Building Blocks / 24.4.7 AccountDetails &lt;AcctDtls&gt; / 24.4.7.2 AccountIdentification &lt;AcctId&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00351.md) | 486–486 |
| [24 sese.001.001.10 TransferOutInstructionV10 / 24.4 Message Building Blocks / 24.4.7 AccountDetails &lt;AcctDtls&gt; / 24.4.7.7 BlockChainAddressOrWallet &lt;BlckChainAdrOrWllt&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00352.md) | 487–487 |
| [24 sese.001.001.10 TransferOutInstructionV10 / 24.4 Message Building Blocks / 24.4.7 AccountDetails &lt;AcctDtls&gt; / 24.4.7.10 DematerialisedIndicator &lt;DmtrlsdInd&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00353.md) | 488–488 |
| [24 sese.001.001.10 TransferOutInstructionV10 / 24.4 Message Building Blocks / 24.4.7 AccountDetails &lt;AcctDtls&gt; / 24.4.7.14 SettlementPartiesDetails &lt;SttlmPtiesDtls&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00354.md) | 489–489 |
| [24 sese.001.001.10 TransferOutInstructionV10 / 24.4 Message Building Blocks / 24.4.7 AccountDetails &lt;AcctDtls&gt; / 24.4.7.14 SettlementPartiesDetails &lt;SttlmPtiesDtls&gt; / 24.4.7.14.2 SettlementTransactionCondition &lt;SttlmTxCond&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00355.md) | 490–491 |
| [24 sese.001.001.10 TransferOutInstructionV10 / 24.4 Message Building Blocks / 24.4.7 AccountDetails &lt;AcctDtls&gt; / 24.4.7.14 SettlementPartiesDetails &lt;SttlmPtiesDtls&gt; / 24.4.7.14.4 DeliveringSideDetails &lt;DlvrgSdDtls&gt; / 24.4.7.14.4.1 Depository &lt;Dpstry&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00356.md) | 492–492 |
| [24 sese.001.001.10 TransferOutInstructionV10 / 24.4 Message Building Blocks / 24.4.7 AccountDetails &lt;AcctDtls&gt; / 24.4.7.14 SettlementPartiesDetails &lt;SttlmPtiesDtls&gt; / 24.4.7.14.4 DeliveringSideDetails &lt;DlvrgSdDtls&gt; / 24.4.7.14.4.2 Party1 &lt;Pty1&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00357.md) | 493–493 |
| [24 sese.001.001.10 TransferOutInstructionV10 / 24.4 Message Building Blocks / 24.4.7 AccountDetails &lt;AcctDtls&gt; / 24.4.7.14 SettlementPartiesDetails &lt;SttlmPtiesDtls&gt; / 24.4.7.14.4 DeliveringSideDetails &lt;DlvrgSdDtls&gt; / 24.4.7.14.4.5 Party4 &lt;Pty4&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00358.md) | 494–496 |
| [24 sese.001.001.10 TransferOutInstructionV10 / 24.4 Message Building Blocks / 24.4.7 AccountDetails &lt;AcctDtls&gt; / 24.4.8.1 Transferee &lt;Trfee&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00359.md) | 497–497 |
| [24 sese.001.001.10 TransferOutInstructionV10 / 24.4 Message Building Blocks / 24.4.7 AccountDetails &lt;AcctDtls&gt; / 24.4.8.2 TransfereeRegisteredAccount &lt;TrfeeRegdAcct&gt; / 24.4.8.2.1 Identification &lt;Id&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00360.md) | 498–498 |
| [24 sese.001.001.10 TransferOutInstructionV10 / 24.4 Message Building Blocks / 24.4.7 AccountDetails &lt;AcctDtls&gt; / 24.4.8.2 TransfereeRegisteredAccount &lt;TrfeeRegdAcct&gt; / 24.4.8.2.6 BlockChainAddressOrWallet &lt;BlckChainAdrOrWllt&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00361.md) | 499–499 |
| [24 sese.001.001.10 TransferOutInstructionV10 / 24.4 Message Building Blocks / 24.4.7 AccountDetails &lt;AcctDtls&gt; / 24.4.8.5 DematerialisedIndicator &lt;DmtrlsdInd&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00362.md) | 500–500 |
| [24 sese.001.001.10 TransferOutInstructionV10 / 24.4 Message Building Blocks / 24.4.7 AccountDetails &lt;AcctDtls&gt; / 24.4.8.9 RequestedSettlementDate &lt;ReqdSttlmDt&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00363.md) | 501–501 |
| [24 sese.001.001.10 TransferOutInstructionV10 / 24.4 Message Building Blocks / 24.4.7 AccountDetails &lt;AcctDtls&gt; / 24.4.8.13 Fees &lt;Fees&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00364.md) | 502–502 |
| [24 sese.001.001.10 TransferOutInstructionV10 / 24.4 Message Building Blocks / 24.4.7 AccountDetails &lt;AcctDtls&gt; / 24.4.8.14 IndividualTax &lt;IndvTax&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00365.md) | 503–503 |
| [24 sese.001.001.10 TransferOutInstructionV10 / 24.4 Message Building Blocks / 24.4.7 AccountDetails &lt;AcctDtls&gt; / 24.4.8.16 SettlementPartiesDetails &lt;SttlmPtiesDtls&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00366.md) | 504–504 |
| [24 sese.001.001.10 TransferOutInstructionV10 / 24.4 Message Building Blocks / 24.4.7 AccountDetails &lt;AcctDtls&gt; / 24.4.8.16 SettlementPartiesDetails &lt;SttlmPtiesDtls&gt; / 24.4.8.16.1 TradeTransactionCondition &lt;TradTxCond&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00367.md) | 505–505 |
| [24 sese.001.001.10 TransferOutInstructionV10 / 24.4 Message Building Blocks / 24.4.7 AccountDetails &lt;AcctDtls&gt; / 24.4.8.16 SettlementPartiesDetails &lt;SttlmPtiesDtls&gt; / 24.4.8.16.3 SecuritiesSettlementSystemIdentification &lt;SctiesSttlmSysId&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00368.md) | 506–506 |
| [24 sese.001.001.10 TransferOutInstructionV10 / 24.4 Message Building Blocks / 24.4.7 AccountDetails &lt;AcctDtls&gt; / 24.4.8.16 SettlementPartiesDetails &lt;SttlmPtiesDtls&gt; / 24.4.8.16.4 ReceivingSideDetails &lt;RcvgSdDtls&gt; / 24.4.8.16.4.1 Depository &lt;Dpstry&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00369.md) | 507–507 |
| [24 sese.001.001.10 TransferOutInstructionV10 / 24.4 Message Building Blocks / 24.4.7 AccountDetails &lt;AcctDtls&gt; / 24.4.8.16 SettlementPartiesDetails &lt;SttlmPtiesDtls&gt; / 24.4.8.16.4 ReceivingSideDetails &lt;RcvgSdDtls&gt; / 24.4.8.16.4.2 Party1 &lt;Pty1&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00370.md) | 508–508 |
| [24 sese.001.001.10 TransferOutInstructionV10 / 24.4 Message Building Blocks / 24.4.7 AccountDetails &lt;AcctDtls&gt; / 24.4.8.16 SettlementPartiesDetails &lt;SttlmPtiesDtls&gt; / 24.4.8.16.4 ReceivingSideDetails &lt;RcvgSdDtls&gt; / 24.4.8.16.4.4 Party3 &lt;Pty3&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00371.md) | 509–509 |
| [24 sese.001.001.10 TransferOutInstructionV10 / 24.4 Message Building Blocks / 24.4.7 AccountDetails &lt;AcctDtls&gt; / 24.4.8.16 SettlementPartiesDetails &lt;SttlmPtiesDtls&gt; / 24.4.8.16.4 ReceivingSideDetails &lt;RcvgSdDtls&gt; / 24.4.8.16.4.6 Party5 &lt;Pty5&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00372.md) | 510–510 |
| [24 sese.001.001.10 TransferOutInstructionV10 / 24.4 Message Building Blocks / 24.4.7 AccountDetails &lt;AcctDtls&gt; / 24.4.8.19 ClientReference &lt;ClntRef&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00373.md) | 511–512 |

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
