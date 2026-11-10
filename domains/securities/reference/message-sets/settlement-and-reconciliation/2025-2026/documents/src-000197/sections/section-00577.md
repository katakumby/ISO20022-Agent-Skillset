---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["25 sese.031.001.11 SecuritiesSettlementConditionModificationStatusAdviceV11", "26.4 Message Building Blocks", "26.4.16 AdditionalPhysicalOrRegistrationDetails <AddtlPhysOrRegnDtls>", "26.4.16.1 CertificationIdentification <CertfctnId>"]
file_pages: [869, 870]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.032.001.13"]
---

# 26.4.16.1 CertificationIdentification <CertfctnId>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 869 to 870.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 869

```text
26.4.16.1  CertificationIdentification <CertfctnId>
Presence: [0..1]
Definition: Identification assigned to a deposit.
Datatype: "Max35Text" on page 2192
26.4.16.2  CertificationDateTime <CertfctnDtTm>
Presence: [0..1]
Definition: Date/time at which the certificates in the deposit were validated by the agent.
CertificationDateTime <CertfctnDtTm> contains one of the following elements (see
"DateAndDateTime2Choice" on page 1441 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 1441
Or}   DateTime <DtTm> [1..1] DateTime 1441
26.4.16.3  RegistrarAccount <RegarAcct>
Presence: [0..1]
Definition: Account at the registrar where financial instruments are registered.
Datatype: "Max35Text" on page 2192
26.4.16.4  CertificateNumber <CertNb>
Presence: [0..*]
Definition: Unique and unambiguous identifier of a certificate assigned by the issuer.
Impacted by: C35 "ISO8532AndIssuerSchemeNameRule"
CertificateNumber <CertNb> contains the following elements (see "SecuritiesCertificate4" on
page 1630 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Number <Nb> [1..1] Text 1631
   Issuer <Issr> [0..1] Text 1631
   SchemeName <SchmeNm> [0..1] Text 1631
Constraints
• ISO8532AndIssuerSchemeNameRule
If Number is ISO 8532 (Format for transmission of certificate numbers), then Issuer and
SchemeName must not be used.
26.4.17 GeneratedReason <GnrtdRsn>
Presence: [0..*]
Approved by the Securities SEG on 27 January 2026 sese.032.001.13
SecuritiesSettlementTransactionGenerationNotificati
onV13
Settlement And Reconciliation - Maintenance 2025 - 2026 869 March 2026
```

## File page 870

```text
Definition: Specifies the reason why the transaction was generated.
GeneratedReason <GnrtdRsn> contains the following elements (see "GeneratedReason5" on
page 1953 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Code <Cd> [1..1] ± 1954
   AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 1954
26.4.18 StatusAndReason <StsAndRsn>
Presence: [0..1]
Definition: Status and reason of the transaction.
Impacted by: C67 "SettlementStatusAndMatchedRule"
StatusAndReason <StsAndRsn> contains the following StatusAndReason50 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ProcessingStatus <PrcgSts> [0..1]  871
{Or     AcknowledgedAccepted <AckdAccptd> [1..1] ± 871
Or     PendingProcessing <PdgPrcg> [1..1] ± 871
Or     Repair <Rpr> [1..1] ± 872
Or     PendingCancellation <PdgCxl> [1..1]  872
{Or       NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 873
Or}       Reason <Rsn> [1..*]  873
         Code <Cd> [1..1]  873
{Or           Code <Cd> [1..1] CodeSet 874
Or}           Proprietary <Prtry> [1..1] ± 874
         AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 874
Or     Proprietary <Prtry> [1..1] ± 874
Or}     CancellationRequested <CxlReqd> [1..1] ± C7 875
   InferredMatchingStatus <IfrrdMtchgSts> [0..1] ± 875
   MatchingStatus <MtchgSts> [0..1] ± 876
   SettlementStatus <SttlmSts> [0..1] ± C46 876
Approved by the Securities SEG on 27 January 2026 sese.032.001.13
SecuritiesSettlementTransactionGenerationNotificati
onV13
Settlement And Reconciliation - Maintenance 2025 - 2026 870 March 2026
```

