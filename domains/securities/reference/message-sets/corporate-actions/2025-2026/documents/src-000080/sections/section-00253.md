---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["6 seev.034.001.16 CorporateActionInstructionStatusAdviceV16", "6.4 Message Building Blocks", "6.4.4 InstructionProcessingStatus <InstrPrcgSts>", "6.4.4.4 Rejected <Rjctd>", "6.4.4.4.2 RejectedReason <RjctdRsn>", "6.4.4.4.2.2 Reason <Rsn>"]
file_pages: [338, 339, 340]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.034.001.16"]
---

# 6.4.4.4.2.2 Reason <Rsn>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 338 to 340.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 338

```text
Datatype: "NoReasonCode" on page 1223
CodeName Name Definition
NORE NoReason No reason to report or no reason
available to report.
6.4.4.4.2.2  Reason <Rsn>
Presence: [1..*]
Definition: Reason why the meeting instruction message or the individual meeting instruction is
rejected.
Impacted by: C5 "AdditionalReasonInforrmationRule"
Reason <Rsn> contains the following RejectedStatusReason63 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ReasonCode <RsnCd> [1..1]  338
{Or     Code <Cd> [1..1] CodeSet 338
Or}     Proprietary <Prtry> [1..1] ± 341
   AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 341
Constraints
• AdditionalReasonInforrmationRule
AdditionalReasonInformation element must not contain information that can be provided in a
structured field unless bilaterally agreed.
6.4.4.4.2.2.1  ReasonCode <RsnCd>
Presence: [1..1]
Definition: Reason for the rejected status.
ReasonCode <RsnCd> contains one of the following RejectedReason68Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 338
Or}   Proprietary <Prtry> [1..1] ± 341
6.4.4.4.2.2.1.1  Code <Cd>
Presence: [1..1]
Definition: Rejection reason specified as a code.
Datatype: "RejectionReason89Code" on page 1237
CodeName Name Definition
ADEA AccountServicerDeadlineMissed Transaction/instruction received after the
account servicer's specified deadline.
Approved by the Securities SEG on 27 January 2026 seev.034.001.16
CorporateActionInstructionStatusAdviceV16
Corporate Actions - Maintenance 2025 - 2026 338 February 2026
```

## File page 339

```text
CodeName Name Definition
CERT IncorrectCertification Instruction is rejected since the provided
certification is incorrect or incomplete.
INVA InvalidForTaxAuthorities For tax reclaim, the reclaim is invalid for
the tax authorities.
OPTY InvalidOptionType Invalid option type.
ULNK InvalidReference Linked reference is unknown.
LACK LackofSecurities Instructed position exceeds the eligible
balance.
LATE MarketDeadlineMissed Received after market deadline.
NMTY Mismatch Mismatch between option number and
option type.
FULL MissingBeneficiaryOwnerDetails Rejected due to missing beneficiary
owner details.
CANC OptionCancelled Option is not valid; it has been cancelled
by the market or service provider, and
cannot be responded to. Any responses
already processed against this option
are considered void and new responses
will be required.
INTV OptionInactive Option is not active and can no longer be
responded to. Any responses already
processed against this option will remain
valid, for example, expired option.
OPNM OptionNumberRejection Unrecognised option number.
OTHR Other Other. See Narrative.
DQUA QuantityRejection Unrecognised or invalid instructed
quantity.
REFT RefusedByTaxAuthorities Reclaim is refused by the tax authorities.
SAFE SafekeepingAccountRejection Unrecognised or invalid message
sender's safekeeping account.
EVNM UnrecognisedIdentification Unrecognised event number.
DQCS AmountRejection Unrecognised or invalid instructed cash
amount.
DQCC CurrencyRejection Invalid instructed currency.
DQAM InstructionTypeRejection Invalid use of instructed amount (QCAS)
or of instructed quantity (QINS)
qualifiers.
IRDQ InvalidUseRoundUpQuantity Instruction is rejected due to invalid use
of the additional round up quantity.
DQBV InvalidBidValue Bid price / basis points / percentage falls
outside of bid range for the event
(generally used in Dutch Auctions or Bid
Tenders).
DQBI InvalidBidIncrement Bid price / basis points / percentage
increments rejected due to invalid bid
increment for the event (generally used
in Dutch Auctions or Bid Tenders).
Approved by the Securities SEG on 27 January 2026 seev.034.001.16
CorporateActionInstructionStatusAdviceV16
Corporate Actions - Maintenance 2025 - 2026 339 February 2026
```

## File page 340

```text
CodeName Name Definition
SHAR ShareholderNumberRejection Unrecognised, missing or invalid
shareholder number.
ITAX IncorrectTaxRate Tax rate provided is incorrect. It falls
outside the acceptable values for that
investment country.
NTAX InconsistentTaxRate Tax rate is not consistent with the
documentation in place.
MTAX MissingTaxRate Tax rate is missing.
ISOL InvalidSolicitationDealerFeeUse Invalid use of solicitation dealer fee
indicator.
BSTR BeforeInstructionPeriod Instruction is submitted before instruction
start date.
CTCT MissingContact Contact information is missing.
DUPL DuplicateInstruction Instruction is rejected due to duplicate
business message identifier.
PROI MissingProtectIdentification Protect identification is required for cover
protect instructions.
PRON NoProtectPrivilege No protect privilege for this event.
PROT MissingProtectDate Protect date is required for cover protect
instructions.
TRTI MissingTransactionType Transaction type is missing or invalid for
protect or cover protect instructions.
IPAW InvalidPaperwork Required paperwork is invalid,
incomplete or missing.
REJA RejectedByIssuerAgent Instruction rejected by the issuer agent.
IPED InstructionPriorToEntitlementDate Instruction was received prior to
entitlement date.
BUMM BuyerProtectionMismatch Counterparty disagreement on the
chosen corporate action outturn.
TRTY IncorrectTransactionType Transaction type is incorrect.
DSNA NoBuyerProtectionAllowed Underlying transaction type/status does
not allow for a buyer protection.
DUCK UnderlyingTransactionCancelled Buyer Protection instruction rejected
since underlying settlement transaction
has been cancelled.
DUST UnderlyingTransactionAlreadySettled Buyer Protection instruction was
rejected, because the underlying
settlement transaction has already been
settled.
ECMD ElectionToCounterpartyMarketDeadlineMissed Received after the election to
counterparty market deadline.
ECRD ElectionToCounterpartyResponseDeadlineMiss
ed
Received after the election to
counterparty response market deadline.
INSA InstructionNotSupportedOrAllowed Instruction is not supported or allowed.
Approved by the Securities SEG on 27 January 2026 seev.034.001.16
CorporateActionInstructionStatusAdviceV16
Corporate Actions - Maintenance 2025 - 2026 340 February 2026
```

