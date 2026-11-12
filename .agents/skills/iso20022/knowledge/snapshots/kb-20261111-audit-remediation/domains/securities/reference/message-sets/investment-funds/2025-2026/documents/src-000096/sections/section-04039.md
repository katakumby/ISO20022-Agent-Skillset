---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.2 Message Datatypes", "66.2.2 CodeSet", "66.2.2.188 RejectedStatusReason12Code"]
file_pages: [5349, 5350, 5351]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.2.2.188 RejectedStatusReason12Code

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 5349 to 5351.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5349

```text
CodeName Name Definition
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
IRIN ReceiversIntermediary Receiver's Intermediary is not
recognised or is invalid.
ICAG DeliveringAgent Delivering agent is not recognised or is
invalid.
IDCU DeliverersCustodian Deliverer's Custodian is not recognised
or is invalid.
IDIN DeliverersIntermediary Deliverer's Intermediary is not
recognised or is invalid.
ICTR InvalidCreditTransfer Credit transfer details are incorrect.
DMON SettlementAmount Settlement Amount is invalid.
DDAT SettlementDate Settlement date or transfer date is not
recognised or is invalid.
NSLA NotCompliantWithSLA Confirmation is not compliant with the
service level agreement.
MEUT MissingEUTaxInformation EU tax information is missing.
MCOM MissingCommission Commission information is missing.
MCHA MissingCharge Charge information is missing.
MTAX MissingTaxInformation Tax information is missing.
NATA NotAllowedtoAmend Amendment of order confirmation not
allowed.
ALAT AmendmentTooLate Amendment of order confirmation too
late.
66.2.2.188  RejectedStatusReason12Code
Definition: Specifies the reason for a transfer or settlement instruction rejected status.
Type: CodeSet
CodeName Name Definition
BLCA AccountBlockedForCorporateAction Investment account is blocked due to a
corporate action.
DOCC AccountBlockedMissingDocuments Investment account is blocked until
certain legal proceedings are completed,
for example, legal documents from the
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5349 May 2026
```

## File page 5350

```text
CodeName Name Definition
successor, legal proceedings due to
bankruptcy.
IAQD AcquisitionDate Acquisition date is not recognised or is
invalid.
ICTN CertificateNumber Certificate number is not recognised or is
invalid.
CYPA CurrentYearPartial Partial transfer of current year is not
allowed, that is, it is not possible to
transfer one asset for the current year as
other assets are held for the current
year.
TREF DuplicateTransferReference Transfer reference is a duplicate of a
previously received transfer.
DSEC FinancialInstrumentIdentification Identification of the security is not
recognised or is invalid.
IDNA FinancialInstrumentIdentificationAndName Identification of the security and the
security name are not the same.
DQUA FinancialInstrumentQuantity Financial instrument quantity is invalid.
FTAX FinancialInstrumentTaxYear Financial instrument is not valid for the
requested tax year.
INID InsufficientInvestorData Investor data is insufficient. Applicable
when the mandated market practice is
not followed.
INAC InvalidAccountServicer Account servicer is not recognised or is
invalid.
CASH InvalidCashAccount Cash account is not recognised or
invalid.
INPM InvalidNewPlanManager New plan manager is not recognised or
is invalid.
INNA InvalidNomineeAccount Nominee account is not recognised or is
invalid.
SAFE InvestmentAccount Investment account identification is not
recognised or is invalid.
INUK InvestorNameAddressUnknown Investor name and address is not
recognised.
LEGL LegallyImpossible Legally impossible to cancel.
NSLA NotCompliantWithSLA Instruction is not compliant with the
service level agreement.
SECU NotEnoughFinancialInstrument There are not enough securities in the
account to process the instruction.
PTNS PartialNotSupported Partial transfer is not supported.
Applicable when tax years are rolled up
and because, for example, a transfer
request for tax year 2000 only is
received, it is not possible to process the
transfer as the investor holds other tax
years as well.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5350 May 2026
```

## File page 5351

```text
CodeName Name Definition
DLVY PhysicalDeliveryImpossible Order contains physical delivery details
but the fund can not be physically
delivered.
DDAT SettlementDate Cash settlement date is not recognised
or is invalid.
ISTP SettlementParties One or several settlement parties are not
recognised or are invalid.
DEPT SettlementPlace Place of settlement is not recognised or
is invalid.
ISAT InvalidISAType ISA type is not recognised or invalid.
OTHR Other Another reason for the status rejected.
NCON NotConvertable The two share classes are not part of the
same fund.
ACLO AssetClosed Asset instructed for transfer is closed.
NASS AssetNotSupported Asset does not support reregistration.
NQTY QuantityBelowMinimum Transfer quantity is too small.
BLTR AccountBlockedForTransfer Investment account is blocked due to a
transfer out of investment funds.
COSE AlreadyExecuted Order or transfer has already been
executed and confirmation has been
sent.
ILLI AssetsIlliquid Assets are illiquid.
BMRV BelowMinimumRetainedAmount Holding will be below the minimum
retained value.
DINV DataInvalid Data in the order or transfer instruction is
invalid.
ICAG DeliveringAgent Delivering agent is not recognised or is
invalid.
IPAC InstructingPartyNotAllowedForAccount Instructing party is not allowed to instruct
for this investment account.
INTE Intermediary Intermediary is not recognised or is
invalid.
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
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5351 May 2026
```

