---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.2 Message Datatypes", "66.2.2 CodeSet", "66.2.2.190 RejectedStatusReason14Code"]
file_pages: [5354, 5355, 5356]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.2.2.190 RejectedStatusReason14Code

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 5354 to 5356.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5354

```text
CodeName Name Definition
DMON InvalidSettlementAmount Unrecognised or invalid settlement
amount.
PRCT PercentageHoldingBreach Percentage holding breach, for example,
PPM rules; taxation rules (ERISA).
IVAG ReceivingAgent Receiving agent is not recognised or is
invalid.
NCRR SettlementAmountCurrency Unrecognised or invalid Settlement
Amount Currency.
DTRD TradeDate Unrecognised or invalid trade date or
requested trade date or future trade
date.
UPAY UnacceptedPaymentMethod Payment method, for example, cheque
or payment card, is not accepted.
URSC UnacceptedRequestedSettlementCurrency Settlement currency requested is not
supported.
NCMP NotCompliantWithMarketPractice Instruction is not compliant with the
relevant market practice.
66.2.2.190  RejectedStatusReason14Code
Definition: Specifies the reason for a rejected status.
Type: CodeSet
CodeName Name Definition
ULNK UnknownLinkagesReference Linked reference is not known.
NSLA NotCompliantWithSLA Instruction is not compliant with the
service level agreement.
CUTO CutOffTime Instruction has been received after the
cut-off time.
NALC NotAllowedToCancel Instructing party is not allowed to request
a cancellation.
LEGL LegallyImpossible Legally impossible to cancel.
ADEA AfterDeadline Instruction was received after the
Receiver's deadline.
NRGM NoCancellationMatch The cancellation request has been
rejected since more than one instruction
match to the cancellation criteria.
66.2.2.191  RejectedStatusReason15Code
Definition: Specifies the reason for a rejected status.
Type: CodeSet
CodeName Name Definition
DDAT SettlementDate Cash settlement date is not recognised
or is invalid.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5354 May 2026
```

## File page 5355

```text
CodeName Name Definition
POIN DifferentValuationPoints Order contains funds that have different
valuation points.
ICAG DeliveringAgent Delivering agent is not recognised or is
invalid.
IDDB DirectDebit Direct debit account identification is not
recognised or is invalid.
INTE Intermediary Intermediary is not recognised or is
invalid.
SAFE InvestmentAccount Investment account identification is not
recognised or is invalid.
IPAY PaymentCard Payment card details are incorrect.
ICTR InvalidCreditTransfer Credit transfer details are incorrect.
DEPT SettlementPlace Place of settlement is not recognised or
is invalid.
IVAG ReceivingAgent Receiving agent is not recognised or is
invalid.
ISAF SafekeepingPlace Safekeeping place is not recognised or
is invalid.
DFOR InvalidSecurityForm Form of the security is wrong, eg, the
form of security is registered not bearer
or vice versa.
DSEC FinancialInstrumentIdentification Identification of the security is not
recognised or is invalid.
BLCA AccountBlockedForCorporateAction Investment account is blocked due to a
corporate action.
BLTR AccountBlockedForTransfer Investment account is blocked due to a
transfer out of investment funds.
DOCC AccountBlockedMissingDocuments Investment account is blocked until
certain legal proceedings are completed,
for example, legal documents from the
successor, legal proceedings due to
bankruptcy.
MONY NotEnoughCash There is not enough cash in the account
to process the instruction.
SECU NotEnoughFinancialInstrument There are not enough securities in the
account to process the instruction.
IDNA FinancialInstrumentIdentificationAndName Identification of the security and the
security name are not the same.
UWAI UnacceptedCommissionWaiving Percentage of commission waiving
exceeds the commission percentage or
commission amount.
UDCY UnacceptedDealCurrency Deal currency is not supported.
UNAV UnacceptedNAVCurrency Net asset value currency is not
supported.
UPAY UnacceptedPaymentMethod Payment method, for example, cheque
or payment card, is not accepted.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5355 May 2026
```

## File page 5356

```text
CodeName Name Definition
URSC UnacceptedRequestedSettlementCurrency Settlement currency requested is not
supported.
SHIG TooHighUnitsOrAmountToSubscribe Quantity of units or amount of money in
the order is too high for a subscription.
SLOW TooLowUnitsOrAmountToSubscribe Quantity of units or amount of money in
the order is too low for a subscription.
ULNK UnknownLinkagesReference Linked reference is not known.
DLVY PhysicalDeliveryImpossible Order contains physical delivery details
but the fund can not be physically
delivered.
ORRF DuplicateOrderReference Order reference is a duplicate of a
previously received order.
IPAC InstructingPartyNotAllowedForAccount Instructing party is not allowed to instruct
for this investment account.
IOTP InvalidOrderType Order type is invalid.
NSLA NotCompliantWithSLA Instruction is not compliant with the
service level agreement.
CUTO CutOffTime Instruction has been received after the
cut-off time.
DQUA FinancialInstrumentQuantity Financial instrument quantity is invalid.
LATE TooLate Instruction was received after market
deadline.
ADEA AfterDeadline Instruction was received after the
Receiver's deadline.
DTRD TradeDate Unrecognised or invalid trade date or
requested trade date or future trade
date.
FEEE FeeOrCommission Unrecognised or invalid fee or
commission.
IEXE SubscriberOrRedeemer Unrecognised or invalid subscriber or
redeemer.
NCRR SettlementAmountCurrency Unrecognised or invalid Settlement
Amount Currency.
PHYS PhysicalSettlement Physical Settlement Impossible.
PLCE PlaceOfTrade Unrecognised or invalid Place of Trade.
SETR SettlementTransaction Unrecognised or invalid Settlement
Transaction.
RTGS RTGSSystem Impossible to use RTGS System.
CASH InvalidCashAccount Cash account is not recognised or
invalid.
DMON InvalidSettlementAmount Unrecognised or invalid settlement
amount.
BMIN BelowMinimumInitialInvestmentAmount Amount of subscription is below the
minimum initial investment amount.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5356 May 2026
```

