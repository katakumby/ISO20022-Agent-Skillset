---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.45 Status", "66.1.45.19 ConfirmationRejectedStatus2", "66.1.45.19.1 Reason <Rsn>", "66.1.45.19.1.1 Code <Cd>"]
file_pages: [5192, 5193]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.45.19.1.1 Code <Cd>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 5192 to 5193.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5192

```text
66.1.45.19.1.1  Code <Cd>
Presence: [1..1]
Definition: Reason for the rejected status expressed as a code.
Datatype: "RejectedConfirmationStatusReason1Code" on page 5347
CodeName Name Definition
DSAF DifferentInvestmentAccountDetails Investment account information not the
same as instructed.
DFIN DifferentFinancialInstrumentDetails Financial instrument information not the
same as instructed.
DBEN DifferentBeneficiaryDetails Beneficiary details is not the same as
instructed.
DPTD DifferentPlaceOfTrade Place of trade not the same as
instructed.
DORD DifferentOrderDateTime Order date time not the same as
instructed.
DCXR DifferentCancellationRight Cancellation right not the same as
instructed.
DUNB DifferentUnitsNumber Units number information not the same
as instructed.
DORT DifferentOrderType Order type information not the same as
instructed.
DROU DifferentRounding Rounding information not the same as
instructed.
DNAM DifferentNetAmount Net amount information not the same as
instructed.
DGAM DifferentGrossAmount Gross amount information not the same
as instructed.
DHRR DifferentHoldingsRedemptionRate Holdings redemption rate not the same
as instructed.
DGRP DifferentGroup1Or2Units Group 1 or 2 units not the same as
instructed.
DINP DifferentIncomePreference Income preference information not the
same as instructed.
DLIR DifferentLetterIntentReference Letter Intent reference information not
the same as instructed.
DARR DifferentAccumulationRightReference Accumulation right reference information
not the same as instructed.
DPDI DifferentPhysicalDeliveryIndicator Physical delivery indicator information
not the same as instructed.
DRSC DifferentRequestedSettlementCurrency Requested settlement currency
information not the same as instructed.
DNAV DifferentRequestedNAVCurrency Requested NAV currency information not
the same as instructed.
DFXD DifferentForeignExchangeDetails Foreign exchange details information not
the same as instructed.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5192 May 2026
```

## File page 5193

```text
CodeName Name Definition
DCHD DifferentChargeDetails Charge details information not the same
as instructed.
DXOD DifferentCommissionDetails Commission details information not the
same as instructed.
DTAD DifferentTaxDetails Tax details information not the same as
instructed.
DPDD DifferentPhysicalDeliveryDetails Physical delivery details information not
the same as instructed.
DSCA DifferentSettlementAndCustodyDetails Settlement and custody details
information not the same as instructed.
DPID DifferentPaymentInstrumentDetails Payment Instrument details information
not the same as instructed.
DSAM DifferentSettlementAmount Settlement amount not the same as
instructed.
DSDT DifferentSettlementDate Settlement date not the same as
instructed.
DEXD DifferentExtensionDetails Extension information not the same as
instructed.
DIMD DifferentIntermediaryDetails Intermediary information not the same as
instructed.
DTRA DifferentTotalRedemptionAmount Total redemption amount not the same
as instructed.
DTSA DifferentTotalSubscriptionAmount Total subscription amount not the same
as instructed.
DACI DifferentAdditionalCashIn Additional cash in not the same as
instructed.
DACO DifferentResultingCashOut Resulting cash out not the same as
instructed.
DPSA DifferentPercentageOfTotalSubscriptionAmount Percentage of total subscription amount
not the same as instructed.
DPRA DifferentPercentageOfTotalRedemptionAmount Percentage of total redemption amount
not the same as instructed.
DLID DifferentLegIdentification Leg Identification not the same as
instructed.
DORF DifferentOrderReference Confirmation is recognised by the
Receiver because the message
reference is identified, but the order
reference is not the same as instructed.
ULNK UnknownLinkagesReference Linked reference is not known.
DREF DuplicateDealReference Deal reference is a duplicate of a
previously received deal reference.
IVAG ReceivingAgent Receiving agent is not recognised or is
invalid.
IRCU ReceiversCustodian Receiver's Custodian is not recognised
or is invalid.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5193 May 2026
```

