---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S LinkReferenceData"
source_ids: ["src-000366"]
source_editions: ["december-2024"]
message_ids: []
heading_path: ["4 reda.047.001.01 SecurityCSDLinkStatusAdviceV01", "4.4 Message Building Blocks", "4.4.2 SecurityCSDLinkStatus <SctyCSDLkSts>", "4.4.2.2 StatusReason <StsRsn>", "4.4.2.2.1 Reason <Rsn>", "4.4.2.2.1.2 Proprietary <Prtry>"]
file_pages: [30]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.047.001.01"]
---

# 4.4.2.2.1.2 Proprietary <Prtry>

Source: [src-000366](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_LinkReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_LinkReferenceData_v1.pdf`. Locator: one-based file pages 30 to 30.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 30

```text
4.4.2.2.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Reason for the status, in a proprietary form.
Datatype: "Max35Text" on page 78
4.4.2.2.2  AdditionalInformation <AddtlInf>
Presence: [0..1]
Definition: Further details on the status reason.
Usage: Additional information can be used for several purposes such as the reporting of repaired
information.
Datatype: "Max140Text" on page 77
4.4.3 SecurityCSDLinkIdentification <SctyCSDLkId>
Presence: [0..1]
Definition: Provides a unique and unambiguous identification for the Security CSD Link.
SecurityCSDLinkIdentification <SctyCSDLkId> contains the following SecurityCSDLink9 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FinancialInstrumentIdentification <FinInstrmId> [1..1] ± C3, C4,
C5, C6,
C7
30
   IssuerInvestorCSD <IssrInvstrCSD> [1..1]  31
{Or     IssuerCSD <IssrCSD> [1..1]  32
{Or       OrganisationIdentification <OrgId> [1..1] ± 32
Or}       CombinedIdentification <CmbndId> [1..1] ± 32
Or}     InvestorCSD <InvstrCSD> [1..1]  33
{Or       OrganisationIdentification <OrgId> [1..1] ± 33
Or}       CombinedIdentification <CmbndId> [1..1] ± 33
   ValidFrom <VldFr> [1..1] ± 33
4.4.3.1  FinancialInstrumentIdentification <FinInstrmId>
Presence: [1..1]
Definition: Identification of a security.
Impacted by: C3 "DescriptionPresenceRule", C4 "DescriptionUsageRule", C5 "ISINGuideline", C6
"ISINPresenceRule", C7 "OtherIdentificationPresenceRule"
Approved by the Securities SEG on 21 November 2024. reda.047.001.01 SecurityCSDLinkStatusAdviceV01
Target2-Securities - Link Reference Data 30 December 2024
```

