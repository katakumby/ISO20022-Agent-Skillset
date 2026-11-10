---
template: false
document_kind: "message-mdr-evidence"
review_status: "needs-review"
domain: "securities"
message_id: "seev.036.001.17"
message_family: "seev.036"
namespace: "urn:iso:std:iso:20022:tech:xsd:seev.036.001.17"
source_ids: ["src-000080"]
source_locations: [{"source_id": "src-000080", "heading": "8 seev.036.001.17 CorporateActionMovementConfirmationV17", "file_pages": [540, 664]}]
limitations: ["PDF text and candidate tables require visual reconciliation; business-role mapping is not inferred from XML names.", "Separate publication statements are retained without version-comparison or silent conflict resolution."]
source_editions: ["February 2026"]
---

# seev.036.001.17 MDR business evidence

The following supplied publications explicitly define this exact message identifier. Functionality text is retained with page locators; detailed definitions, rules, tables and figures remain in focused source sections. This page does not substitute one message version for another.

## src-000080 — 8 seev.036.001.17 CorporateActionMovementConfirmationV17

[src-000080](../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf); file pp540–664; publication February 2026. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000080, 8 seev.036.001.17 CorporateActionMovementConfirmationV17, Functionality, file p540.**

Scope
The CorporateActionMovementConfirmation message is sent by an account servicer to an account
owner or its designated agent to confirm the posting of securities or cash as a result of a corporate
action event.
Usage
The message may also be used to:
- re-send a message previously sent (the sub-function of the message is Duplicate),
- provide a third party with a copy of a message for information (the sub-function of the message is
Copy),
- re-send to a third party a copy of a message for information (the sub-function of the message is Copy
Duplicate), using the relevant elements in the business application header (BAH).
Outline
The CorporateActionMovementConfirmationV17 MessageDefinition is composed of 17
MessageBuildingBlocks:
A. Pagination
Page number of the message and continuation indicator to indicate that the multi-part notification is
to continue or that the message is the last page of the multi-part notification.
B. MovementConfirmationIdentification
Unique Identification of the group of corporate action movement confirmation messages when the
movement confirmation is split in multiple (paginated) messages.
C. NotificationIdentification
Identification of a previously sent notification document.
D. MovementPreliminaryAdviceIdentification
Identification of a previously sent movement preliminary advice document.
E. InstructionIdentification
Identification of a related instruction document.
F. OtherDocumentIdentification
Identification of other documents as well as the document number.
G. EventsLinkage
Identification of another corporate action event that needs to be closely linked to the processing of
the event notified in this document.
Approved by the Securities SEG on 27 January 2026 seev.036.001.17
CorporateActionMovementConfirmationV17
Corporate Actions - Maintenance 2025 - 2026 540 February 2026

**src-000080, 8 seev.036.001.17 CorporateActionMovementConfirmationV17, Functionality, file p541.**

H. TransactionIdentification
Transaction type and identification information.
I. CorporateActionGeneralInformation
General information about the corporate action event.
J. AccountDetails
General information about the safekeeping account, owner and account balance.
K. CorporateActionDetails
Information about the corporate action event.
L. CorporateActionConfirmationDetails
Information about the corporate action option.
M. AdditionalInformation
Provides additional information.
N. IssuerAgent
Party appointed to administer the event on behalf of the issuer company/offeror. The party may be
contacted for more information about the event.
O. PayingAgent
Agent (principal or fiscal paying agent) appointed to execute the payment for the corporate action
event on behalf of the issuer company/offeror.
P. SubPayingAgent
Sub-agent appointed to execute the payment for the corporate action event on behalf of the issuer
company/offeror.
Q. SupplementaryData
Additional information that can not be captured in the structured fields and/or any other specific
block.
Approved by the Securities SEG on 27 January 2026 seev.036.001.17
CorporateActionMovementConfirmationV17
Corporate Actions - Maintenance 2025 - 2026 541 February 2026

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/corporate-actions/2025-2026/documents/src-000080/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [8 seev.036.001.17 CorporateActionMovementConfirmationV17](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00410.md) | 540–541 |
| [8 seev.036.001.17 CorporateActionMovementConfirmationV17 / 8.2 Structure](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00411.md) | 542–549 |
| [8 seev.036.001.17 CorporateActionMovementConfirmationV17 / 8.3 Constraints](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00412.md) | 550–557 |
| [8 seev.036.001.17 CorporateActionMovementConfirmationV17 / 8.4 Message Building Blocks](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00413.md) | 558–558 |
| [8 seev.036.001.17 CorporateActionMovementConfirmationV17 / 8.4 Message Building Blocks / 8.4.4 MovementPreliminaryAdviceIdentification &lt;MvmntPrlimryAdvcId&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00414.md) | 559–559 |
| [8 seev.036.001.17 CorporateActionMovementConfirmationV17 / 8.4 Message Building Blocks / 8.4.7 EventsLinkage &lt;EvtsLkg&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00415.md) | 560–560 |
| [8 seev.036.001.17 CorporateActionMovementConfirmationV17 / 8.4 Message Building Blocks / 8.4.9 CorporateActionGeneralInformation &lt;CorpActnGnlInf&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00416.md) | 561–561 |
| [8 seev.036.001.17 CorporateActionMovementConfirmationV17 / 8.4 Message Building Blocks / 8.4.9 CorporateActionGeneralInformation &lt;CorpActnGnlInf&gt; / 8.4.9.4 EventType &lt;EvtTp&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00417.md) | 562–562 |
| [8 seev.036.001.17 CorporateActionMovementConfirmationV17 / 8.4 Message Building Blocks / 8.4.9 CorporateActionGeneralInformation &lt;CorpActnGnlInf&gt; / 8.4.9.6 FractionalQuantity &lt;FrctnlQty&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00418.md) | 563–563 |
| [8 seev.036.001.17 CorporateActionMovementConfirmationV17 / 8.4 Message Building Blocks / 8.4.10 AccountDetails &lt;AcctDtls&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00419.md) | 564–564 |
| [8 seev.036.001.17 CorporateActionMovementConfirmationV17 / 8.4 Message Building Blocks / 8.4.10 AccountDetails &lt;AcctDtls&gt; / 8.4.10.1 SafekeepingAccount &lt;SfkpgAcct&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00420.md) | 565–565 |
| [8 seev.036.001.17 CorporateActionMovementConfirmationV17 / 8.4 Message Building Blocks / 8.4.10 AccountDetails &lt;AcctDtls&gt; / 8.4.10.4 SafekeepingPlace &lt;SfkpgPlc&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00421.md) | 566–566 |
| [8 seev.036.001.17 CorporateActionMovementConfirmationV17 / 8.4 Message Building Blocks / 8.4.10 AccountDetails &lt;AcctDtls&gt; / 8.4.10.5 Balance &lt;Bal&gt; / 8.4.10.5.1 ConfirmedBalance &lt;ConfdBal&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00422.md) | 567–567 |
| [8 seev.036.001.17 CorporateActionMovementConfirmationV17 / 8.4 Message Building Blocks / 8.4.10 AccountDetails &lt;AcctDtls&gt; / 8.4.10.5 Balance &lt;Bal&gt; / 8.4.10.5.2 TotalEligibleBalance &lt;TtlElgblBal&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00423.md) | 568–568 |
| [8 seev.036.001.17 CorporateActionMovementConfirmationV17 / 8.4 Message Building Blocks / 8.4.10 AccountDetails &lt;AcctDtls&gt; / 8.4.10.5 Balance &lt;Bal&gt; / 8.4.10.5.6 CollateralOutBalance &lt;CollOutBal&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00424.md) | 569–569 |
| [8 seev.036.001.17 CorporateActionMovementConfirmationV17 / 8.4 Message Building Blocks / 8.4.10 AccountDetails &lt;AcctDtls&gt; / 8.4.10.5 Balance &lt;Bal&gt; / 8.4.10.5.9 PendingReceiptBalance &lt;PdgRctBal&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00425.md) | 570–570 |
| [8 seev.036.001.17 CorporateActionMovementConfirmationV17 / 8.4 Message Building Blocks / 8.4.10 AccountDetails &lt;AcctDtls&gt; / 8.4.10.5 Balance &lt;Bal&gt; / 8.4.10.5.12 StreetPositionBalance &lt;StrtPosBal&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00426.md) | 571–571 |
| [8 seev.036.001.17 CorporateActionMovementConfirmationV17 / 8.4 Message Building Blocks / 8.4.10 AccountDetails &lt;AcctDtls&gt; / 8.4.10.5 Balance &lt;Bal&gt; / 8.4.10.5.15 RegisteredBalance &lt;RegdBal&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00427.md) | 572–572 |
| [8 seev.036.001.17 CorporateActionMovementConfirmationV17 / 8.4 Message Building Blocks / 8.4.11 CorporateActionDetails &lt;CorpActnDtls&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00428.md) | 573–573 |
| [8 seev.036.001.17 CorporateActionMovementConfirmationV17 / 8.4 Message Building Blocks / 8.4.11 CorporateActionDetails &lt;CorpActnDtls&gt; / 8.4.11.1 DateDetails &lt;DtDtls&gt; / 8.4.11.1.2 ExDividendDate &lt;ExDvddDt&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00429.md) | 574–574 |
| [8 seev.036.001.17 CorporateActionMovementConfirmationV17 / 8.4 Message Building Blocks / 8.4.11 CorporateActionDetails &lt;CorpActnDtls&gt; / 8.4.11.4 FollowingEventTypeIndicator &lt;FllwngEvtTpInd&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00430.md) | 575–581 |
| [8 seev.036.001.17 CorporateActionMovementConfirmationV17 / 8.4 Message Building Blocks / 8.4.12 CorporateActionConfirmationDetails &lt;CorpActnConfDtls&gt; / 8.4.12.1 OptionNumber &lt;OptnNb&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00431.md) | 582–582 |
| [8 seev.036.001.17 CorporateActionMovementConfirmationV17 / 8.4 Message Building Blocks / 8.4.12 CorporateActionConfirmationDetails &lt;CorpActnConfDtls&gt; / 8.4.12.3 OptionFeatures &lt;OptnFeatrs&gt; / 8.4.12.3.1 Code &lt;Cd&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00432.md) | 583–583 |
| [8 seev.036.001.17 CorporateActionMovementConfirmationV17 / 8.4 Message Building Blocks / 8.4.12 CorporateActionConfirmationDetails &lt;CorpActnConfDtls&gt; / 8.4.12.4 FractionDisposition &lt;FrctnDspstn&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00433.md) | 584–584 |
| [8 seev.036.001.17 CorporateActionMovementConfirmationV17 / 8.4 Message Building Blocks / 8.4.12 CorporateActionConfirmationDetails &lt;CorpActnConfDtls&gt; / 8.4.12.6 DateDetails &lt;DtDtls&gt; / 8.4.12.6.2 TradingDate &lt;TradgDt&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00434.md) | 585–586 |
| [8 seev.036.001.17 CorporateActionMovementConfirmationV17 / 8.4 Message Building Blocks / 8.4.12 CorporateActionConfirmationDetails &lt;CorpActnConfDtls&gt; / 8.4.12.7 RateAndAmountDetails &lt;RateAndAmtDtls&gt; / 8.4.12.7.1 GrossDistributionRate &lt;GrssDstrbtnRate&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00435.md) | 587–587 |
| [8 seev.036.001.17 CorporateActionMovementConfirmationV17 / 8.4 Message Building Blocks / 8.4.12 CorporateActionConfirmationDetails &lt;CorpActnConfDtls&gt; / 8.4.12.7 RateAndAmountDetails &lt;RateAndAmtDtls&gt; / 8.4.12.7.2 NetDistributionRate &lt;NetDstrbtnRate&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00436.md) | 588–588 |
| [8 seev.036.001.17 CorporateActionMovementConfirmationV17 / 8.4 Message Building Blocks / 8.4.12 CorporateActionConfirmationDetails &lt;CorpActnConfDtls&gt; / 8.4.12.7 RateAndAmountDetails &lt;RateAndAmtDtls&gt; / 8.4.12.7.4 MaximumAllowedOversubscriptionRate &lt;MaxAllwdOvrsbcptRate&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00437.md) | 589–589 |
| [8 seev.036.001.17 CorporateActionMovementConfirmationV17 / 8.4 Message Building Blocks / 8.4.12 CorporateActionConfirmationDetails &lt;CorpActnConfDtls&gt; / 8.4.12.7 RateAndAmountDetails &lt;RateAndAmtDtls&gt; / 8.4.12.7.7 SecondLevelTax &lt;ScndLvlTax&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00438.md) | 590–590 |
| [8 seev.036.001.17 CorporateActionMovementConfirmationV17 / 8.4 Message Building Blocks / 8.4.12 CorporateActionConfirmationDetails &lt;CorpActnConfDtls&gt; / 8.4.12.7 RateAndAmountDetails &lt;RateAndAmtDtls&gt; / 8.4.12.7.9 TaxableIncomePerDividendShare &lt;TaxblIncmPerDvddShr&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00439.md) | 591–591 |
| [8 seev.036.001.17 CorporateActionMovementConfirmationV17 / 8.4 Message Building Blocks / 8.4.12 CorporateActionConfirmationDetails &lt;CorpActnConfDtls&gt; / 8.4.12.8 PriceDetails &lt;PricDtls&gt; / 8.4.12.8.2 OverSubscriptionDepositPrice &lt;OverSbcptDpstPric&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00440.md) | 592–592 |
| [8 seev.036.001.17 CorporateActionMovementConfirmationV17 / 8.4 Message Building Blocks / 8.4.12 CorporateActionConfirmationDetails &lt;CorpActnConfDtls&gt; / 8.4.12.10 SecuritiesMovementDetails &lt;SctiesMvmntDtls&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00441.md) | 593–595 |
| [8 seev.036.001.17 CorporateActionMovementConfirmationV17 / 8.4 Message Building Blocks / 8.4.12 CorporateActionConfirmationDetails &lt;CorpActnConfDtls&gt; / 8.4.12.10 SecuritiesMovementDetails &lt;SctiesMvmntDtls&gt; / 8.4.12.10.1 FinancialInstrumentIdentification &lt;FinInstrmId&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00442.md) | 596–596 |
| [8 seev.036.001.17 CorporateActionMovementConfirmationV17 / 8.4 Message Building Blocks / 8.4.12 CorporateActionConfirmationDetails &lt;CorpActnConfDtls&gt; / 8.4.12.10 SecuritiesMovementDetails &lt;SctiesMvmntDtls&gt; / 8.4.12.10.2 CreditDebitIndicator &lt;CdtDbtInd&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00443.md) | 597–597 |
| [8 seev.036.001.17 CorporateActionMovementConfirmationV17 / 8.4 Message Building Blocks / 8.4.12 CorporateActionConfirmationDetails &lt;CorpActnConfDtls&gt; / 8.4.12.10 SecuritiesMovementDetails &lt;SctiesMvmntDtls&gt; / 8.4.12.10.5 IssuerOfferorTaxabilityIndicator &lt;IssrOfferrTaxbltyInd&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00444.md) | 598–598 |
| [8 seev.036.001.17 CorporateActionMovementConfirmationV17 / 8.4 Message Building Blocks / 8.4.12 CorporateActionConfirmationDetails &lt;CorpActnConfDtls&gt; / 8.4.12.10 SecuritiesMovementDetails &lt;SctiesMvmntDtls&gt; / 8.4.12.10.7 OtherIncomeType &lt;OthrIncmTp&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00445.md) | 599–599 |
| [8 seev.036.001.17 CorporateActionMovementConfirmationV17 / 8.4 Message Building Blocks / 8.4.12 CorporateActionConfirmationDetails &lt;CorpActnConfDtls&gt; / 8.4.12.10 SecuritiesMovementDetails &lt;SctiesMvmntDtls&gt; / 8.4.12.10.10 PostingQuantity &lt;PstngQty&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00446.md) | 600–600 |
| [8 seev.036.001.17 CorporateActionMovementConfirmationV17 / 8.4 Message Building Blocks / 8.4.12 CorporateActionConfirmationDetails &lt;CorpActnConfDtls&gt; / 8.4.12.10 SecuritiesMovementDetails &lt;SctiesMvmntDtls&gt; / 8.4.12.10.13 CurrencyOption &lt;CcyOptn&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00447.md) | 601–601 |
| [8 seev.036.001.17 CorporateActionMovementConfirmationV17 / 8.4 Message Building Blocks / 8.4.12 CorporateActionConfirmationDetails &lt;CorpActnConfDtls&gt; / 8.4.12.10 SecuritiesMovementDetails &lt;SctiesMvmntDtls&gt; / 8.4.12.10.14 DateDetails &lt;DtDtls&gt; / 8.4.12.10.14.2 AvailableDate &lt;AvlblDt&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00448.md) | 602–602 |
| [8 seev.036.001.17 CorporateActionMovementConfirmationV17 / 8.4 Message Building Blocks / 8.4.12 CorporateActionConfirmationDetails &lt;CorpActnConfDtls&gt; / 8.4.12.10 SecuritiesMovementDetails &lt;SctiesMvmntDtls&gt; / 8.4.12.10.14 DateDetails &lt;DtDtls&gt; / 8.4.12.10.14.5 EarliestPaymentDate &lt;EarlstPmtDt&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00449.md) | 603–603 |
| [8 seev.036.001.17 CorporateActionMovementConfirmationV17 / 8.4 Message Building Blocks / 8.4.12 CorporateActionConfirmationDetails &lt;CorpActnConfDtls&gt; / 8.4.12.10 SecuritiesMovementDetails &lt;SctiesMvmntDtls&gt; / 8.4.12.10.15 RateDetails &lt;RateDtls&gt; / 8.4.12.10.15.1 AdditionalQuantityForSubscribedResultantSecurities &lt;AddtlQtyForSbcbdRsltntScties&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00450.md) | 604–604 |
| [8 seev.036.001.17 CorporateActionMovementConfirmationV17 / 8.4 Message Building Blocks / 8.4.12 CorporateActionConfirmationDetails &lt;CorpActnConfDtls&gt; / 8.4.12.10 SecuritiesMovementDetails &lt;SctiesMvmntDtls&gt; / 8.4.12.10.15 RateDetails &lt;RateDtls&gt; / 8.4.12.10.15.3 NewToOld &lt;NewToOd&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00451.md) | 605–605 |
| [8 seev.036.001.17 CorporateActionMovementConfirmationV17 / 8.4 Message Building Blocks / 8.4.12 CorporateActionConfirmationDetails &lt;CorpActnConfDtls&gt; / 8.4.12.10 SecuritiesMovementDetails &lt;SctiesMvmntDtls&gt; / 8.4.12.10.15 RateDetails &lt;RateDtls&gt; / 8.4.12.10.15.5 FiscalStamp &lt;FsclStmp&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00452.md) | 606–606 |
| [8 seev.036.001.17 CorporateActionMovementConfirmationV17 / 8.4 Message Building Blocks / 8.4.12 CorporateActionConfirmationDetails &lt;CorpActnConfDtls&gt; / 8.4.12.10 SecuritiesMovementDetails &lt;SctiesMvmntDtls&gt; / 8.4.12.10.15 RateDetails &lt;RateDtls&gt; / 8.4.12.10.15.10 SecondLevelTax &lt;ScndLvlTax&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00453.md) | 607–607 |
| [8 seev.036.001.17 CorporateActionMovementConfirmationV17 / 8.4 Message Building Blocks / 8.4.12 CorporateActionConfirmationDetails &lt;CorpActnConfDtls&gt; / 8.4.12.10 SecuritiesMovementDetails &lt;SctiesMvmntDtls&gt; / 8.4.12.10.16 PriceDetails &lt;PricDtls&gt; / 8.4.12.10.16.1 CashInLieuOfSharePrice &lt;CshInLieuOfShrPric&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00454.md) | 608–608 |
| [8 seev.036.001.17 CorporateActionMovementConfirmationV17 / 8.4 Message Building Blocks / 8.4.12 CorporateActionConfirmationDetails &lt;CorpActnConfDtls&gt; / 8.4.12.10 SecuritiesMovementDetails &lt;SctiesMvmntDtls&gt; / 8.4.12.10.16 PriceDetails &lt;PricDtls&gt; / 8.4.12.10.16.2 IndicativeOrMarketPrice &lt;IndctvOrMktPric&gt; / 8.4.12.10.16.2.1 IndicativePrice &lt;IndctvPric&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00455.md) | 609–609 |
| [8 seev.036.001.17 CorporateActionMovementConfirmationV17 / 8.4 Message Building Blocks / 8.4.12 CorporateActionConfirmationDetails &lt;CorpActnConfDtls&gt; / 8.4.12.10 SecuritiesMovementDetails &lt;SctiesMvmntDtls&gt; / 8.4.12.10.16 PriceDetails &lt;PricDtls&gt; / 8.4.12.10.16.5 GenericCashPriceReceivedPerProduct &lt;GncCshPricRcvdPerPdct&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00456.md) | 610–610 |
| [8 seev.036.001.17 CorporateActionMovementConfirmationV17 / 8.4 Message Building Blocks / 8.4.12 CorporateActionConfirmationDetails &lt;CorpActnConfDtls&gt; / 8.4.12.10 SecuritiesMovementDetails &lt;SctiesMvmntDtls&gt; / 8.4.12.10.17 AmountDetails &lt;AmtDtls&gt; / 8.4.12.10.17.1 WithholdingTaxAmount &lt;WhldgTaxAmt&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00457.md) | 611–611 |
| [8 seev.036.001.17 CorporateActionMovementConfirmationV17 / 8.4 Message Building Blocks / 8.4.12 CorporateActionConfirmationDetails &lt;CorpActnConfDtls&gt; / 8.4.12.10 SecuritiesMovementDetails &lt;SctiesMvmntDtls&gt; / 8.4.12.10.18 ReceivingSettlementParties &lt;RcvgSttlmPties&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00458.md) | 612–612 |
| [8 seev.036.001.17 CorporateActionMovementConfirmationV17 / 8.4 Message Building Blocks / 8.4.12 CorporateActionConfirmationDetails &lt;CorpActnConfDtls&gt; / 8.4.12.11 CashMovementDetails &lt;CshMvmntDtls&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00459.md) | 613–617 |
| [8 seev.036.001.17 CorporateActionMovementConfirmationV17 / 8.4 Message Building Blocks / 8.4.12 CorporateActionConfirmationDetails &lt;CorpActnConfDtls&gt; / 8.4.12.11 CashMovementDetails &lt;CshMvmntDtls&gt; / 8.4.12.11.1 CreditDebitIndicator &lt;CdtDbtInd&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00460.md) | 618–618 |
| [8 seev.036.001.17 CorporateActionMovementConfirmationV17 / 8.4 Message Building Blocks / 8.4.12 CorporateActionConfirmationDetails &lt;CorpActnConfDtls&gt; / 8.4.12.11 CashMovementDetails &lt;CshMvmntDtls&gt; / 8.4.12.11.3 IssuerOfferorTaxabilityIndicator &lt;IssrOfferrTaxbltyInd&gt; / 8.4.12.11.3.2 Proprietary &lt;Prtry&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00461.md) | 619–619 |
| [8 seev.036.001.17 CorporateActionMovementConfirmationV17 / 8.4 Message Building Blocks / 8.4.12 CorporateActionConfirmationDetails &lt;CorpActnConfDtls&gt; / 8.4.12.11 CashMovementDetails &lt;CshMvmntDtls&gt; / 8.4.12.11.7 CountryOfIncomeSource &lt;CtryOfIncmSrc&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00462.md) | 620–620 |
| [8 seev.036.001.17 CorporateActionMovementConfirmationV17 / 8.4 Message Building Blocks / 8.4.12 CorporateActionConfirmationDetails &lt;CorpActnConfDtls&gt; / 8.4.12.11 CashMovementDetails &lt;CshMvmntDtls&gt; / 8.4.12.11.8 Account &lt;Acct&gt; / 8.4.12.11.8.2 ChargesAccount &lt;ChrgsAcct&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00463.md) | 621–621 |
| [8 seev.036.001.17 CorporateActionMovementConfirmationV17 / 8.4 Message Building Blocks / 8.4.12 CorporateActionConfirmationDetails &lt;CorpActnConfDtls&gt; / 8.4.12.11 CashMovementDetails &lt;CshMvmntDtls&gt; / 8.4.12.11.10 AmountDetails &lt;AmtDtls&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00464.md) | 622–623 |
| [8 seev.036.001.17 CorporateActionMovementConfirmationV17 / 8.4 Message Building Blocks / 8.4.12 CorporateActionConfirmationDetails &lt;CorpActnConfDtls&gt; / 8.4.12.11 CashMovementDetails &lt;CshMvmntDtls&gt; / 8.4.12.11.10 AmountDetails &lt;AmtDtls&gt; / 8.4.12.11.10.1 PostingAmount &lt;PstngAmt&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00465.md) | 624–624 |
| [8 seev.036.001.17 CorporateActionMovementConfirmationV17 / 8.4 Message Building Blocks / 8.4.12 CorporateActionConfirmationDetails &lt;CorpActnConfDtls&gt; / 8.4.12.11 CashMovementDetails &lt;CshMvmntDtls&gt; / 8.4.12.11.10 AmountDetails &lt;AmtDtls&gt; / 8.4.12.11.10.2 GrossAmount &lt;GrssAmt&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00466.md) | 625–625 |
| [8 seev.036.001.17 CorporateActionMovementConfirmationV17 / 8.4 Message Building Blocks / 8.4.12 CorporateActionConfirmationDetails &lt;CorpActnConfDtls&gt; / 8.4.12.11 CashMovementDetails &lt;CshMvmntDtls&gt; / 8.4.12.11.10 AmountDetails &lt;AmtDtls&gt; / 8.4.12.11.10.4 SolicitationFees &lt;SlctnFees&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00467.md) | 626–626 |
| [8 seev.036.001.17 CorporateActionMovementConfirmationV17 / 8.4 Message Building Blocks / 8.4.12 CorporateActionConfirmationDetails &lt;CorpActnConfDtls&gt; / 8.4.12.11 CashMovementDetails &lt;CshMvmntDtls&gt; / 8.4.12.11.10 AmountDetails &lt;AmtDtls&gt; / 8.4.12.11.10.7 InterestAmount &lt;IntrstAmt&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00468.md) | 627–627 |
| [8 seev.036.001.17 CorporateActionMovementConfirmationV17 / 8.4 Message Building Blocks / 8.4.12 CorporateActionConfirmationDetails &lt;CorpActnConfDtls&gt; / 8.4.12.11 CashMovementDetails &lt;CshMvmntDtls&gt; / 8.4.12.11.10 AmountDetails &lt;AmtDtls&gt; / 8.4.12.11.10.9 IndemnityAmount &lt;IndmntyAmt&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00469.md) | 628–628 |
| [8 seev.036.001.17 CorporateActionMovementConfirmationV17 / 8.4 Message Building Blocks / 8.4.12 CorporateActionConfirmationDetails &lt;CorpActnConfDtls&gt; / 8.4.12.11 CashMovementDetails &lt;CshMvmntDtls&gt; / 8.4.12.11.10 AmountDetails &lt;AmtDtls&gt; / 8.4.12.11.10.11 ReinvestmentAmount &lt;RinvstmtAmt&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00470.md) | 629–629 |
| [8 seev.036.001.17 CorporateActionMovementConfirmationV17 / 8.4 Message Building Blocks / 8.4.12 CorporateActionConfirmationDetails &lt;CorpActnConfDtls&gt; / 8.4.12.11 CashMovementDetails &lt;CshMvmntDtls&gt; / 8.4.12.11.10 AmountDetails &lt;AmtDtls&gt; / 8.4.12.11.10.14 SundryOrOtherAmount &lt;SndryOrOthrAmt&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00471.md) | 630–630 |
| [8 seev.036.001.17 CorporateActionMovementConfirmationV17 / 8.4 Message Building Blocks / 8.4.12 CorporateActionConfirmationDetails &lt;CorpActnConfDtls&gt; / 8.4.12.11 CashMovementDetails &lt;CshMvmntDtls&gt; / 8.4.12.11.10 AmountDetails &lt;AmtDtls&gt; / 8.4.12.11.10.16 TaxDeferredAmount &lt;TaxDfrrdAmt&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00472.md) | 631–631 |
| [8 seev.036.001.17 CorporateActionMovementConfirmationV17 / 8.4 Message Building Blocks / 8.4.12 CorporateActionConfirmationDetails &lt;CorpActnConfDtls&gt; / 8.4.12.11 CashMovementDetails &lt;CshMvmntDtls&gt; / 8.4.12.11.10 AmountDetails &lt;AmtDtls&gt; / 8.4.12.11.10.19 TaxReclaimAmount &lt;TaxRclmAmt&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00473.md) | 632–632 |
| [8 seev.036.001.17 CorporateActionMovementConfirmationV17 / 8.4 Message Building Blocks / 8.4.12 CorporateActionConfirmationDetails &lt;CorpActnConfDtls&gt; / 8.4.12.11 CashMovementDetails &lt;CshMvmntDtls&gt; / 8.4.12.11.10 AmountDetails &lt;AmtDtls&gt; / 8.4.12.11.10.21 AdditionalTaxAmount &lt;AddtlTaxAmt&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00474.md) | 633–633 |
| [8 seev.036.001.17 CorporateActionMovementConfirmationV17 / 8.4 Message Building Blocks / 8.4.12 CorporateActionConfirmationDetails &lt;CorpActnConfDtls&gt; / 8.4.12.11 CashMovementDetails &lt;CshMvmntDtls&gt; / 8.4.12.11.10 AmountDetails &lt;AmtDtls&gt; / 8.4.12.11.10.24 FiscalStampAmount &lt;FsclStmpAmt&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00475.md) | 634–634 |
| [8 seev.036.001.17 CorporateActionMovementConfirmationV17 / 8.4 Message Building Blocks / 8.4.12 CorporateActionConfirmationDetails &lt;CorpActnConfDtls&gt; / 8.4.12.11 CashMovementDetails &lt;CshMvmntDtls&gt; / 8.4.12.11.10 AmountDetails &lt;AmtDtls&gt; / 8.4.12.11.10.26 PayingAgentCommissionAmount &lt;PngAgtComssnAmt&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00476.md) | 635–635 |
| [8 seev.036.001.17 CorporateActionMovementConfirmationV17 / 8.4 Message Building Blocks / 8.4.12 CorporateActionConfirmationDetails &lt;CorpActnConfDtls&gt; / 8.4.12.11 CashMovementDetails &lt;CshMvmntDtls&gt; / 8.4.12.11.10 AmountDetails &lt;AmtDtls&gt; / 8.4.12.11.10.29 ShippingFeesAmount &lt;ShppgFeesAmt&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00477.md) | 636–636 |
| [8 seev.036.001.17 CorporateActionMovementConfirmationV17 / 8.4 Message Building Blocks / 8.4.12 CorporateActionConfirmationDetails &lt;CorpActnConfDtls&gt; / 8.4.12.11 CashMovementDetails &lt;CshMvmntDtls&gt; / 8.4.12.11.10 AmountDetails &lt;AmtDtls&gt; / 8.4.12.11.10.31 CashAmountBroughtForward &lt;CshAmtBrghtFwd&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00478.md) | 637–637 |
| [8 seev.036.001.17 CorporateActionMovementConfirmationV17 / 8.4 Message Building Blocks / 8.4.12 CorporateActionConfirmationDetails &lt;CorpActnConfDtls&gt; / 8.4.12.11 CashMovementDetails &lt;CshMvmntDtls&gt; / 8.4.12.11.10 AmountDetails &lt;AmtDtls&gt; / 8.4.12.11.10.34 NotionalTaxAmount &lt;NtnlTaxAmt&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00479.md) | 638–638 |
| [8 seev.036.001.17 CorporateActionMovementConfirmationV17 / 8.4 Message Building Blocks / 8.4.12 CorporateActionConfirmationDetails &lt;CorpActnConfDtls&gt; / 8.4.12.11 CashMovementDetails &lt;CshMvmntDtls&gt; / 8.4.12.11.10 AmountDetails &lt;AmtDtls&gt; / 8.4.12.11.10.36 OriginalAmount &lt;OrgnlAmt&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00480.md) | 639–639 |
| [8 seev.036.001.17 CorporateActionMovementConfirmationV17 / 8.4 Message Building Blocks / 8.4.12 CorporateActionConfirmationDetails &lt;CorpActnConfDtls&gt; / 8.4.12.11 CashMovementDetails &lt;CshMvmntDtls&gt; / 8.4.12.11.10 AmountDetails &lt;AmtDtls&gt; / 8.4.12.11.10.39 IncomePortion &lt;IncmPrtn&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00481.md) | 640–640 |
| [8 seev.036.001.17 CorporateActionMovementConfirmationV17 / 8.4 Message Building Blocks / 8.4.12 CorporateActionConfirmationDetails &lt;CorpActnConfDtls&gt; / 8.4.12.11 CashMovementDetails &lt;CshMvmntDtls&gt; / 8.4.12.11.10 AmountDetails &lt;AmtDtls&gt; / 8.4.12.11.10.41 EUTaxRetentionAmount &lt;EUTaxRtntnAmt&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00482.md) | 641–641 |
| [8 seev.036.001.17 CorporateActionMovementConfirmationV17 / 8.4 Message Building Blocks / 8.4.12 CorporateActionConfirmationDetails &lt;CorpActnConfDtls&gt; / 8.4.12.11 CashMovementDetails &lt;CshMvmntDtls&gt; / 8.4.12.11.10 AmountDetails &lt;AmtDtls&gt; / 8.4.12.11.10.44 FATCATaxAmount &lt;FATCATaxAmt&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00483.md) | 642–642 |
| [8 seev.036.001.17 CorporateActionMovementConfirmationV17 / 8.4 Message Building Blocks / 8.4.12 CorporateActionConfirmationDetails &lt;CorpActnConfDtls&gt; / 8.4.12.11 CashMovementDetails &lt;CshMvmntDtls&gt; / 8.4.12.11.10 AmountDetails &lt;AmtDtls&gt; / 8.4.12.11.10.46 BackUpWithholdingTaxAmount &lt;BckUpWhldgTaxAmt&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00484.md) | 643–643 |
| [8 seev.036.001.17 CorporateActionMovementConfirmationV17 / 8.4 Message Building Blocks / 8.4.12 CorporateActionConfirmationDetails &lt;CorpActnConfDtls&gt; / 8.4.12.11 CashMovementDetails &lt;CshMvmntDtls&gt; / 8.4.12.11.10 AmountDetails &lt;AmtDtls&gt; / 8.4.12.11.10.49 DeemedAmount &lt;DmdAmt&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00485.md) | 644–644 |
| [8 seev.036.001.17 CorporateActionMovementConfirmationV17 / 8.4 Message Building Blocks / 8.4.12 CorporateActionConfirmationDetails &lt;CorpActnConfDtls&gt; / 8.4.12.11 CashMovementDetails &lt;CshMvmntDtls&gt; / 8.4.12.11.10 AmountDetails &lt;AmtDtls&gt; / 8.4.12.11.10.51 DeemedDividendAmount &lt;DmdDvddAmt&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00486.md) | 645–645 |
| [8 seev.036.001.17 CorporateActionMovementConfirmationV17 / 8.4 Message Building Blocks / 8.4.12 CorporateActionConfirmationDetails &lt;CorpActnConfDtls&gt; / 8.4.12.11 CashMovementDetails &lt;CshMvmntDtls&gt; / 8.4.12.11.10 AmountDetails &lt;AmtDtls&gt; / 8.4.12.11.10.54 DeemedRoyaltiesAmount &lt;DmdRyltsAmt&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00487.md) | 646–646 |
| [8 seev.036.001.17 CorporateActionMovementConfirmationV17 / 8.4 Message Building Blocks / 8.4.12 CorporateActionConfirmationDetails &lt;CorpActnConfDtls&gt; / 8.4.12.11 CashMovementDetails &lt;CshMvmntDtls&gt; / 8.4.12.11.10 AmountDetails &lt;AmtDtls&gt; / 8.4.12.11.10.56 RefundedSubscriptionAmount &lt;RfnddSbcptAmt&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00488.md) | 647–647 |
| [8 seev.036.001.17 CorporateActionMovementConfirmationV17 / 8.4 Message Building Blocks / 8.4.12 CorporateActionConfirmationDetails &lt;CorpActnConfDtls&gt; / 8.4.12.11 CashMovementDetails &lt;CshMvmntDtls&gt; / 8.4.12.11.11 DateDetails &lt;DtDtls&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00489.md) | 648–648 |
| [8 seev.036.001.17 CorporateActionMovementConfirmationV17 / 8.4 Message Building Blocks / 8.4.12 CorporateActionConfirmationDetails &lt;CorpActnConfDtls&gt; / 8.4.12.11 CashMovementDetails &lt;CshMvmntDtls&gt; / 8.4.12.11.11 DateDetails &lt;DtDtls&gt; / 8.4.12.11.11.5 PaymentDate &lt;PmtDt&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00490.md) | 649–649 |
| [8 seev.036.001.17 CorporateActionMovementConfirmationV17 / 8.4 Message Building Blocks / 8.4.12 CorporateActionConfirmationDetails &lt;CorpActnConfDtls&gt; / 8.4.12.11 CashMovementDetails &lt;CshMvmntDtls&gt; / 8.4.12.11.14 RateAndAmountDetails &lt;RateAndAmtDtls&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00491.md) | 650–651 |
| [8 seev.036.001.17 CorporateActionMovementConfirmationV17 / 8.4 Message Building Blocks / 8.4.12 CorporateActionConfirmationDetails &lt;CorpActnConfDtls&gt; / 8.4.12.11 CashMovementDetails &lt;CshMvmntDtls&gt; / 8.4.12.11.14 RateAndAmountDetails &lt;RateAndAmtDtls&gt; / 8.4.12.11.14.1 AdditionalTax &lt;AddtlTax&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00492.md) | 652–652 |
| [8 seev.036.001.17 CorporateActionMovementConfirmationV17 / 8.4 Message Building Blocks / 8.4.12 CorporateActionConfirmationDetails &lt;CorpActnConfDtls&gt; / 8.4.12.11 CashMovementDetails &lt;CshMvmntDtls&gt; / 8.4.12.11.14 RateAndAmountDetails &lt;RateAndAmtDtls&gt; / 8.4.12.11.14.2 ChargesFees &lt;ChrgsFees&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00493.md) | 653–653 |
| [8 seev.036.001.17 CorporateActionMovementConfirmationV17 / 8.4 Message Building Blocks / 8.4.12 CorporateActionConfirmationDetails &lt;CorpActnConfDtls&gt; / 8.4.12.11 CashMovementDetails &lt;CshMvmntDtls&gt; / 8.4.12.11.14 RateAndAmountDetails &lt;RateAndAmtDtls&gt; / 8.4.12.11.14.5 EarlySolicitationFeeRate &lt;EarlySlctnFeeRate&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00494.md) | 654–654 |
| [8 seev.036.001.17 CorporateActionMovementConfirmationV17 / 8.4 Message Building Blocks / 8.4.12 CorporateActionConfirmationDetails &lt;CorpActnConfDtls&gt; / 8.4.12.11 CashMovementDetails &lt;CshMvmntDtls&gt; / 8.4.12.11.14 RateAndAmountDetails &lt;RateAndAmtDtls&gt; / 8.4.12.11.14.7 GrossInterestRateUsedForPayment &lt;GrssIntrstRateUsdForPmt&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00495.md) | 655–655 |
| [8 seev.036.001.17 CorporateActionMovementConfirmationV17 / 8.4 Message Building Blocks / 8.4.12 CorporateActionConfirmationDetails &lt;CorpActnConfDtls&gt; / 8.4.12.11 CashMovementDetails &lt;CshMvmntDtls&gt; / 8.4.12.11.14 RateAndAmountDetails &lt;RateAndAmtDtls&gt; / 8.4.12.11.14.9 ApplicableRate &lt;AplblRate&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00496.md) | 656–656 |
| [8 seev.036.001.17 CorporateActionMovementConfirmationV17 / 8.4 Message Building Blocks / 8.4.12 CorporateActionConfirmationDetails &lt;CorpActnConfDtls&gt; / 8.4.12.11 CashMovementDetails &lt;CshMvmntDtls&gt; / 8.4.12.11.14 RateAndAmountDetails &lt;RateAndAmtDtls&gt; / 8.4.12.11.14.11 TaxCreditRate &lt;TaxCdtRate&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00497.md) | 657–657 |
| [8 seev.036.001.17 CorporateActionMovementConfirmationV17 / 8.4 Message Building Blocks / 8.4.12 CorporateActionConfirmationDetails &lt;CorpActnConfDtls&gt; / 8.4.12.11 CashMovementDetails &lt;CshMvmntDtls&gt; / 8.4.12.11.14 RateAndAmountDetails &lt;RateAndAmtDtls&gt; / 8.4.12.11.14.14 TaxOnIncome &lt;TaxOnIncm&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00498.md) | 658–658 |
| [8 seev.036.001.17 CorporateActionMovementConfirmationV17 / 8.4 Message Building Blocks / 8.4.12 CorporateActionConfirmationDetails &lt;CorpActnConfDtls&gt; / 8.4.12.11 CashMovementDetails &lt;CshMvmntDtls&gt; / 8.4.12.11.14 RateAndAmountDetails &lt;RateAndAmtDtls&gt; / 8.4.12.11.14.18 DeemedRate &lt;DmdRate&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00499.md) | 659–659 |
| [8 seev.036.001.17 CorporateActionMovementConfirmationV17 / 8.4 Message Building Blocks / 8.4.12 CorporateActionConfirmationDetails &lt;CorpActnConfDtls&gt; / 8.4.12.11 CashMovementDetails &lt;CshMvmntDtls&gt; / 8.4.12.11.15 PriceDetails &lt;PricDtls&gt; / 8.4.12.11.15.1 GenericCashPricePaidPerProduct &lt;GncCshPricPdPerPdct&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00500.md) | 660–660 |
| [8 seev.036.001.17 CorporateActionMovementConfirmationV17 / 8.4 Message Building Blocks / 8.4.12 CorporateActionConfirmationDetails &lt;CorpActnConfDtls&gt; / 8.4.12.11 CashMovementDetails &lt;CshMvmntDtls&gt; / 8.4.12.11.15 PriceDetails &lt;PricDtls&gt; / 8.4.12.11.15.3 CashInLieuOfSharePrice &lt;CshInLieuOfShrPric&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00501.md) | 661–661 |
| [8 seev.036.001.17 CorporateActionMovementConfirmationV17 / 8.4 Message Building Blocks / 8.4.13 AdditionalInformation &lt;AddtlInf&gt; / 8.4.13.1 AdditionalText &lt;AddtlTxt&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00502.md) | 662–662 |
| [8 seev.036.001.17 CorporateActionMovementConfirmationV17 / 8.4 Message Building Blocks / 8.4.15 PayingAgent &lt;PngAgt&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00503.md) | 663–664 |

## Scoped participants and related business flows

| Reference | Kind | Source |
| --- | --- | --- |
| [Designated agent of the corporate-action account owner](../../../../../shared/reference/participants/participant-corporate-actions-designated-agent.md) | participant | src-000080 |
| [Account Owner](../../../../../shared/reference/participants/participant-src-000079-account-owner.md) | participant | src-000079, src-000080 |
| [Account Servicer](../../../../../shared/reference/participants/participant-src-000079-account-servicer.md) | participant | src-000079, src-000080 |
| [Beneficial Owner](../../../../../shared/reference/participants/participant-src-000079-beneficial-owner.md) | participant | src-000079 |
| [Broker](../../../../../shared/reference/participants/participant-src-000079-broker.md) | participant | src-000079 |
| [Clearing Agent](../../../../../shared/reference/participants/participant-src-000079-clearing-agent.md) | participant | src-000079 |
| [CSD / ICSD](../../../../../shared/reference/participants/participant-src-000079-csd-icsd.md) | participant | src-000079 |
| [CSD](../../../../../shared/reference/participants/participant-src-000079-csd.md) | participant | src-000079 |
| [Fund Manager](../../../../../shared/reference/participants/participant-src-000079-fund-manager.md) | participant | src-000079 |
| [Global Custodian](../../../../../shared/reference/participants/participant-src-000079-global-custodian.md) | participant | src-000079 |
| [ICSD](../../../../../shared/reference/participants/participant-src-000079-icsd.md) | participant | src-000079 |
| [Institutional Investor](../../../../../shared/reference/participants/participant-src-000079-institutional-investor.md) | participant | src-000079 |
| [Issuer Agent](../../../../../shared/reference/participants/participant-src-000079-issuer-agent.md) | participant | src-000079 |
| [Issuer](../../../../../shared/reference/participants/participant-src-000079-issuer.md) | participant | src-000079 |
| [Market Data Provider](../../../../../shared/reference/participants/participant-src-000079-market-data-provider.md) | participant | src-000079 |
| [Stock Exchange](../../../../../shared/reference/participants/participant-src-000079-stock-exchange.md) | participant | src-000079 |
| [Sub-Custodian](../../../../../shared/reference/participants/participant-src-000079-sub-custodian.md) | participant | src-000079 |
| [Event Notification](../../message-sets/corporate-actions/2025-2026/flows/flow-src-000079-p145-event-notification.md) | business-flow | src-000079 |
| [Eligibility / Entitlement Notification](../../message-sets/corporate-actions/2025-2026/flows/flow-src-000079-p146-eligibility-entitlement-notification.md) | business-flow | src-000079 |
| [Reminder](../../message-sets/corporate-actions/2025-2026/flows/flow-src-000079-p147-reminder.md) | business-flow | src-000079 |
| [Election](../../message-sets/corporate-actions/2025-2026/flows/flow-src-000079-p149-election.md) | business-flow | src-000079 |
| [Movement Preliminary Advice / Final Entitlement process](../../message-sets/corporate-actions/2025-2026/flows/flow-src-000079-p150-movement-preliminary-advice-final-entitlement-process.md) | business-flow | src-000079 |
| [Movement Confirmation](../../message-sets/corporate-actions/2025-2026/flows/flow-src-000079-p152-movement-confirmation.md) | business-flow | src-000079 |
| [Movement Reversal](../../message-sets/corporate-actions/2025-2026/flows/flow-src-000079-p153-movement-reversal.md) | business-flow | src-000079, src-000080 |
| [Cancellation](../../message-sets/corporate-actions/2025-2026/flows/flow-src-000079-p154-cancellation.md) | business-flow | src-000079 |
| [Status Reporting](../../message-sets/corporate-actions/2025-2026/flows/flow-src-000079-p155-status-reporting.md) | business-flow | src-000079 |
| [Generic Corporate Action Process (Non Elective Event)](../../message-sets/corporate-actions/2025-2026/flows/flow-src-000079-p177-generic-corporate-action-process-non-elective-event.md) | business-flow | src-000079 |
| [Instruction Process (Elective Event)](../../message-sets/corporate-actions/2025-2026/flows/flow-src-000079-p180-instruction-process-elective-event.md) | business-flow | src-000079 |
| [Instruction Cancellation Request Process (Elective Event)](../../message-sets/corporate-actions/2025-2026/flows/flow-src-000079-p183-instruction-cancellation-request-process-elective-event.md) | business-flow | src-000079 |
| [Reminder Process](../../message-sets/corporate-actions/2025-2026/flows/flow-src-000079-p185-reminder-process.md) | business-flow | src-000079 |
| [Instruction Reporting Process](../../message-sets/corporate-actions/2025-2026/flows/flow-src-000079-p187-instruction-reporting-process.md) | business-flow | src-000079 |
| [Movement Preliminary Advice Process](../../message-sets/corporate-actions/2025-2026/flows/flow-src-000079-p189-movement-preliminary-advice-process.md) | business-flow | src-000079 |
| [Movement Preliminary Advice Cancellation Process](../../message-sets/corporate-actions/2025-2026/flows/flow-src-000079-p191-movement-preliminary-advice-cancellation-process.md) | business-flow | src-000079 |
| [Corporate Action Event Withdrawal Process](../../message-sets/corporate-actions/2025-2026/flows/flow-src-000079-p195-corporate-action-event-withdrawal-process.md) | business-flow | src-000079 |
| [Announcement](../../message-sets/corporate-actions/2025-2026/flows/flow-src-000079-p207-announcement.md) | business-flow | src-000079, src-000080 |
| [Announcement and Cancellation of Event](../../message-sets/corporate-actions/2025-2026/flows/flow-src-000079-p217-announcement-and-cancellation-of-event.md) | business-flow | src-000079, src-000080 |
| [Announcement and Cancellation due to Processing Error](../../message-sets/corporate-actions/2025-2026/flows/flow-src-000079-p223-announcement-and-cancellation-due-to-processing-error.md) | business-flow | src-000079, src-000080 |
| [Final Entitlement Replacement Scenario](../../message-sets/corporate-actions/2025-2026/flows/flow-src-000079-p229-final-entitlement-replacement-scenario.md) | business-flow | src-000079, src-000080 |
| [Election and Final Entitlement](../../message-sets/corporate-actions/2025-2026/flows/flow-src-000079-p238-election-and-final-entitlement.md) | business-flow | src-000079, src-000080 |
| [Election and Final Entitlement Cancellation Scenario](../../message-sets/corporate-actions/2025-2026/flows/flow-src-000079-p243-election-and-final-entitlement-cancellation-scenario.md) | business-flow | src-000079, src-000080 |
| [Election and Final Entitlement Replacement](../../message-sets/corporate-actions/2025-2026/flows/flow-src-000079-p251-election-and-final-entitlement-replacement.md) | business-flow | src-000079, src-000080 |
| [Reminder](../../message-sets/corporate-actions/2025-2026/flows/flow-src-000079-p257-reminder.md) | business-flow | src-000079, src-000080 |
| [Confirmation](../../message-sets/corporate-actions/2025-2026/flows/flow-src-000079-p265-confirmation.md) | business-flow | src-000079, src-000080 |
| [Instruction Reporting](../../message-sets/corporate-actions/2025-2026/flows/flow-src-000079-p282-instruction-reporting.md) | business-flow | src-000079, src-000080 |
| [Narrative](../../message-sets/corporate-actions/2025-2026/flows/flow-src-000079-p285-narrative.md) | business-flow | src-000079, src-000080 |

[Canonical message](index.md) · [Schema structure](structure.md) · [Known gaps](../../../../../tracking/issues.md)
