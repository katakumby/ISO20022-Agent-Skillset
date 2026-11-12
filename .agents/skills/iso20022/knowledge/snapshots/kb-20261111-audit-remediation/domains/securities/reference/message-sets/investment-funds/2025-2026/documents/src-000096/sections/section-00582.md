---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["31 sese.008.001.09 ReversalOfTransferInConfirmationV09", "32.3 Constraints"]
file_pages: [787, 788, 789, 790]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.009.001.09"]
---

# 32.3 Constraints

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 787 to 790.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 787

```text
32.3 Constraints
C1 ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the
message containing the currency is exchanged. Valid active currency codes are registered with
the ISO 4217 Maintenance Agency, consist of three (3) contiguous letters, and are not yet
withdrawn on the day the message containing the Currency is exchanged.
C2 AnyBIC
Only a valid Business identifier code is allowed. Business identifier codes for financial or non-
financial institutions are registered and published by the ISO 9362 Registration Authority in the
ISO directory of BICs, and consists of eight (8) or eleven (11) contiguous characters.
C3 Country
The code is checked against the list of country names obtained from the United Nations (ISO
3166, Alpha-2 code).
C4 ExtensionRule
This component may not be used without the explicit approval of the Registration Authority and
without strict usage rules published by the Registration Authority.
C5 HoldingTransferCurrencyGuideline
When cash is transferred in a currency other than that of the cash, the currency should be
specified in TransferCurrency.
C6 IdentificationGuideline
When an ISIN code exists, it is strongly recommended that the ISIN be used.
C7 OtherReferenceRule
Reference/OtherReference should be used to reference a transfer instruction or a transfer
cancellation request 'message' sent in a proprietary way or used for a system reference. If
Reference/OtherReference is present, Reference/OtherReference/MessageName must contain
'fax' or 'phone' or 'email', etc.
C8 PreviousReferenceRule
If Reference/PreviousReference/MessageName is present, it must start with sese.001,
sese.002, sese.005, sese.006, sese.012 or sese.014.
32.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
32.4.1 MessageIdentification <MsgId>
Presence: [1..1]
Definition: Reference that uniquely identifies the message from a business application standpoint.
Approved by the Securities SEG on 27 January 2026 sese.009.001.09
RequestForTransferStatusReportV09
Investment Funds - Maintenance 2025 - 2026 787 May 2026
```

## File page 788

```text
MessageIdentification <MsgId> contains the following elements (see "MessageIdentification1" on
page 4548 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4548
   CreationDateTime <CreDtTm> [1..1] DateTime 4549
32.4.2 RequestDetails <ReqDtls>
Presence: [1..*]
Definition: Information to identify the transfer for which the status is requested.
Impacted by: C7 "OtherReferenceRule", C8 "PreviousReferenceRule"
Approved by the Securities SEG on 27 January 2026 sese.009.001.09
RequestForTransferStatusReportV09
Investment Funds - Maintenance 2025 - 2026 788 May 2026
```

## File page 789

```text
RequestDetails <ReqDtls> contains the following MessageAndBusinessReference14 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reference <Ref> [0..1]  791
{Or     PreviousReference <PrvsRef> [1..1] ± 791
Or}     OtherReference <OthrRef> [1..1] ± 791
   TypeOfRequest <TpOfReq> [0..1]  791
{Or     Code <Cd> [1..1] CodeSet 792
Or}     Proprietary <Prtry> [1..1] ± 792
   MasterReference <MstrRef> [0..1] Text 792
   TransferReference <TrfRef> [1..1] ± 792
   ClientReference <ClntRef> [0..1] ± 793
   CancellationReference <CxlRef> [0..1] Text 793
   Instrument <Instrm> [0..1]  793
{Or     Security <Scty> [1..1]  C6 794
       Identification <Id> [1..1]  795
{Or         ISIN <ISIN> [1..1] IdentifierSet 796
Or         SEDOL <SEDOL> [1..1] IdentifierSet 796
Or         CUSIP <CUSIP> [1..1] IdentifierSet 797
Or         RIC <RIC> [1..1] IdentifierSet 797
Or         TickerSymbol <TckrSymb> [1..1] IdentifierSet 797
Or         Bloomberg <Blmbrg> [1..1] IdentifierSet 797
Or         CTA <CTA> [1..1] IdentifierSet 797
Or         QUICK <QUICK> [1..1] IdentifierSet 797
Or         Wertpapier <Wrtppr> [1..1] IdentifierSet 797
Or         Dutch <Dtch> [1..1] IdentifierSet 798
Or         Valoren <Vlrn> [1..1] IdentifierSet 798
Or         Sicovam <SCVM> [1..1] IdentifierSet 798
Or         Belgian <Belgn> [1..1] IdentifierSet 798
Or         Common <Cmon> [1..1] IdentifierSet 798
Or         DTI <DTI> [1..1] IdentifierSet 798
Or}         OtherProprietaryIdentification <OthrPrtryId> [1..1]  798
           Identification <Id> [1..1] Text 799
           IdentificationSource <IdSrc> [1..1] ± 799
Approved by the Securities SEG on 27 January 2026 sese.009.001.09
RequestForTransferStatusReportV09
Investment Funds - Maintenance 2025 - 2026 789 May 2026
```

## File page 790

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
       Name <Nm> [0..1] Text 799
       ShortName <ShrtNm> [0..1] Text 799
       ClassificationType <ClssfctnTp> [0..1] ± 799
Or     CashAsset <CshAsst> [1..1] ± C5 799
Or}     OtherAsset <OthrAsst> [1..1] ± 800
   InvestmentAccountDetails <InvstmtAcctDtls> [0..1]  800
     OwnerIdentification <OwnrId> [0..1] ± 801
     AccountIdentification <AcctId> [0..1] Text 801
     AccountDesignation <AcctDsgnt> [0..1] Text 801
     AccountName <AcctNm> [0..1] Text 802
     Type <Tp> [0..1] ± 802
     Servicer <Svcr> [0..1] ± 802
     SubAccountDetails <SubAcctDtls> [0..1] ± 802
     BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 803
   IntermediaryInformation <IntrmyInf> [0..*] ± 803
   QueryInformation <QryInf> [0..*]  803
     QueryType <QryTp> [0..1] ± 804
     Query <Qry> [1..1] Text 804
     QueryReason <QryRsn> [0..1] Text 804
     RejectionReason <RjctnRsn> [0..1]  804
{Or       Code <Cd> [1..1] CodeSet 805
Or}       Proprietary <Prtry> [1..1] ± 807
   RequestIssuer <ReqIssr> [0..1] ± 807
   RequestRecipient <ReqRcpt> [0..1] ± 807
Constraints
• OtherReferenceRule
Reference/OtherReference should be used to reference a transfer instruction or a transfer
cancellation request 'message' sent in a proprietary way or used for a system reference. If
Reference/OtherReference is present, Reference/OtherReference/MessageName must contain 'fax'
or 'phone' or 'email', etc.
• PreviousReferenceRule
If Reference/PreviousReference/MessageName is present, it must start with sese.001, sese.002,
sese.005, sese.006, sese.012 or sese.014.
Approved by the Securities SEG on 27 January 2026 sese.009.001.09
RequestForTransferStatusReportV09
Investment Funds - Maintenance 2025 - 2026 790 May 2026
```

