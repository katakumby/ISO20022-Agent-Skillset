---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["56 setr.016.001.05 OrderInstructionStatusReportV05", "56.4 Message Building Blocks", "56.4.3.1 OrderDetailsReport <OrdrDtlsRpt>", "56.4.3.1.2 OrderStatus <OrdrSts>", "56.4.3.1.2.4 Rejected <Rjctd>"]
file_pages: [4131, 4132, 4133]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.016.001.05"]
---

# 56.4.3.1.2.4 Rejected <Rjctd>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4131 to 4133.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4131

```text
56.4.3.1.2.4  Rejected <Rjctd>
Presence: [1..10]
Definition: Status of all the orders in the order message is rejected. This status is used for orders that
have not been accepted or entered in an order book.
Impacted by: C18 "RejectedElementRule"
Rejected <Rjctd> contains the following RejectedStatus14 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reason <Rsn> [0..1]  4131
{Or     Code <Cd> [1..1] CodeSet 4131
Or}     Proprietary <Prtry> [1..1] ± 4134
   AdditionalInformation <AddtlInf> [0..1] Text 4134
Constraints
• RejectedElementRule
Either Reason or AdditionalInformation must be present. Both may be present.
56.4.3.1.2.4.1  Reason <Rsn>
Presence: [0..1]
Definition: Reason for the rejected status.
Reason <Rsn> contains one of the following RejectedReason67Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 4131
Or}   Proprietary <Prtry> [1..1] ± 4134
56.4.3.1.2.4.1.1  Code <Cd>
Presence: [1..1]
Definition: Rejected reason expressed as a code.
Datatype: "RejectedStatusReason15Code" on page 0
CodeName Name Definition
DDAT SettlementDate Cash settlement date is not recognised
or is invalid.
POIN DifferentValuationPoints Order contains funds that have different
valuation points.
ICAG DeliveringAgent Delivering agent is not recognised or is
invalid.
IDDB DirectDebit Direct debit account identification is not
recognised or is invalid.
INTE Intermediary Intermediary is not recognised or is
invalid.
Approved by the Securities SEG on 27 January 2026 setr.016.001.05 OrderInstructionStatusReportV05
Investment Funds - Maintenance 2025 - 2026 4131 May 2026
```

## File page 4132

```text
CodeName Name Definition
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
URSC UnacceptedRequestedSettlementCurrency Settlement currency requested is not
supported.
SHIG TooHighUnitsOrAmountToSubscribe Quantity of units or amount of money in
the order is too high for a subscription.
SLOW TooLowUnitsOrAmountToSubscribe Quantity of units or amount of money in
the order is too low for a subscription.
ULNK UnknownLinkagesReference Linked reference is not known.
Approved by the Securities SEG on 27 January 2026 setr.016.001.05 OrderInstructionStatusReportV05
Investment Funds - Maintenance 2025 - 2026 4132 May 2026
```

## File page 4133

```text
CodeName Name Definition
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
INSU InsufficientCapacity Insufficient capacity.
PRCT PercentageHoldingBreach Percentage holding breach, for example,
PPM rules; taxation rules (ERISA).
BMRA BelowMinimumRedemptionAmount Amount is below the minimum
redemption amount.
BMRV BelowMinimumRetainedAmount Holding will be below the minimum
retained value.
Approved by the Securities SEG on 27 January 2026 setr.016.001.05 OrderInstructionStatusReportV05
Investment Funds - Maintenance 2025 - 2026 4133 May 2026
```

