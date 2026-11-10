---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["56 setr.016.001.05 OrderInstructionStatusReportV05", "56.4 Message Building Blocks", "56.4.3.3 SwitchOrderDetailsReport <SwtchOrdrDtlsRpt>", "56.4.3.3.7 OrderStatus <OrdrSts>", "56.4.3.3.7.4 Rejected <Rjctd>", "56.4.3.3.7.4.1 Reason <Rsn>", "56.4.3.3.7.4.1.1 Code <Cd>"]
file_pages: [4180, 4181]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.016.001.05"]
---

# 56.4.3.3.7.4.1.1 Code <Cd>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4180 to 4181.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4180

```text
Definition: Reason for the rejected status.
Reason <Rsn> contains one of the following RejectedReason67Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 4180
Or}   Proprietary <Prtry> [1..1] ± 4182
56.4.3.3.7.4.1.1  Code <Cd>
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
Approved by the Securities SEG on 27 January 2026 setr.016.001.05 OrderInstructionStatusReportV05
Investment Funds - Maintenance 2025 - 2026 4180 May 2026
```

## File page 4181

```text
CodeName Name Definition
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
Approved by the Securities SEG on 27 January 2026 setr.016.001.05 OrderInstructionStatusReportV05
Investment Funds - Maintenance 2025 - 2026 4181 May 2026
```

