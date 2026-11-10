---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["33 sese.010.001.07 TransferCancellationStatusReportV07", "34.4 Message Building Blocks", "34.4.4 StatusReport <StsRpt>", "34.4.4.6 TransferStatus <TrfSts>", "34.4.4.6.5 Rejected <Rjctd>", "34.4.4.6.5.1 Reason <Rsn>"]
file_pages: [845, 846]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.011.001.10"]
---

# 34.4.4.6.5.1 Reason <Rsn>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 845 to 846.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 845

```text
Rejected <Rjctd> contains the following RejectionReason56 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reason <Rsn> [1..1]  845
{Or     Code <Cd> [1..1] CodeSet 845
Or}     Proprietary <Prtry> [1..1] ± 847
   AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 848
Constraints
• OtherRule
If Reason/Code/OTHR (Other) is present, then AdditionReasonInformation must be present and the
reason for the rejection status must be provided.
34.4.4.6.5.1  Reason <Rsn>
Presence: [1..1]
Definition: Reason for the rejected status.
Reason <Rsn> contains one of the following RejectedReason45Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 845
Or}   Proprietary <Prtry> [1..1] ± 847
34.4.4.6.5.1.1  Code <Cd>
Presence: [1..1]
Definition: Rejected reason expressed as a code.
Datatype: "RejectedStatusReason13Code" on page 5352
CodeName Name Definition
BLCA AccountBlockedForCorporateAction Investment account is blocked due to a
corporate action.
DOCC AccountBlockedMissingDocuments Investment account is blocked until
certain legal proceedings are completed,
for example, legal documents from the
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
Approved by the Securities SEG on 27 January 2026 sese.011.001.10
TransferInstructionStatusReportV10
Investment Funds - Maintenance 2025 - 2026 845 May 2026
```

## File page 846

```text
CodeName Name Definition
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
Approved by the Securities SEG on 27 January 2026 sese.011.001.10
TransferInstructionStatusReportV10
Investment Funds - Maintenance 2025 - 2026 846 May 2026
```

