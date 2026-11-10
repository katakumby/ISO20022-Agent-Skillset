---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["64 reda.047.001.01 SecurityCSDLinkStatusAdviceV01", "64.4 Message Building Blocks", "64.4.2 SecurityCSDLinkStatus <SctyCSDLkSts>", "64.4.2.2 StatusReason <StsRsn>", "64.4.2.2.1 Reason <Rsn>", "64.4.2.2.1.2 Proprietary <Prtry>"]
file_pages: [2364]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.047.001.01"]
---

# 64.4.2.2.1.2 Proprietary <Prtry>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 2364 to 2364.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2364

```text
64.4.2.2.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Reason for the status, in a proprietary form.
Datatype: "Max35Text" on page 3328
64.4.2.2.2  AdditionalInformation <AddtlInf>
Presence: [0..1]
Definition: Further details on the status reason.
Usage: Additional information can be used for several purposes such as the reporting of repaired
information.
Datatype: "Max140Text" on page 3326
64.4.3 SecurityCSDLinkIdentification <SctyCSDLkId>
Presence: [0..1]
Definition: Provides a unique and unambiguous identification for the Security CSD Link.
SecurityCSDLinkIdentification <SctyCSDLkId> contains the following SecurityCSDLink9 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FinancialInstrumentIdentification <FinInstrmId> [1..1] ± C3, C4,
C5, C6,
C7
2364
   IssuerInvestorCSD <IssrInvstrCSD> [1..1]  2365
{Or     IssuerCSD <IssrCSD> [1..1]  2366
{Or       OrganisationIdentification <OrgId> [1..1] ± 2366
Or}       CombinedIdentification <CmbndId> [1..1] ± 2366
Or}     InvestorCSD <InvstrCSD> [1..1]  2367
{Or       OrganisationIdentification <OrgId> [1..1] ± 2367
Or}       CombinedIdentification <CmbndId> [1..1] ± 2367
   ValidFrom <VldFr> [1..1] ± 2367
64.4.3.1  FinancialInstrumentIdentification <FinInstrmId>
Presence: [1..1]
Definition: Identification of a security.
Impacted by: C3 "DescriptionPresenceRule", C4 "DescriptionUsageRule", C5 "ISINGuideline", C6
"ISINPresenceRule", C7 "OtherIdentificationPresenceRule"
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.047.001.01 SecurityCSDLinkStatusAdviceV01
Target2-Securities 2364 August 2026
```

