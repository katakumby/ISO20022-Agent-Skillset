---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["42 reda.022.001.02 PartyModificationRequestV02", "42.4 Message Building Blocks", "42.4.3 Modification <Mod>", "42.4.3.2 RequestedModification <ReqdMod>", "42.4.3.2.5 TechnicalAddress <TechAdr>"]
file_pages: [2149]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.022.001.02"]
---

# 42.4.3.2.5 TechnicalAddress <TechAdr>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 2149 to 2149.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2149

```text
ContactDetails <CtctDtls> contains the following elements (see "Contact14" on page 3080 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   NamePrefix <NmPrfx> [0..1] CodeSet 3081
   Name <Nm> [0..1] Text 3081
   PhoneNumber <PhneNb> [0..1] Text 3082
   MobileNumber <MobNb> [0..1] Text 3082
   FaxNumber <FaxNb> [0..1] Text 3082
   URLAddress <URLAdr> [0..1] Text 3082
   EmailAddress <EmailAdr> [0..1] Text 3082
   EmailPurpose <EmailPurp> [0..1] Text 3082
   JobTitle <JobTitl> [0..1] Text 3082
   Responsibility <Rspnsblty> [0..1] Text 3082
   Department <Dept> [0..1] Text 3083
   Other <Othr> [0..*]  3083
     ChannelType <ChanlTp> [1..1] Text 3083
     Identification <Id> [0..1] Text 3083
   PreferredMethod <PrefrdMtd> [0..1] CodeSet 3083
   ValidFrom <VldFr> [0..1] Date 3084
   ValidTo <VldTo> [0..1] Date 3084
42.4.3.2.5  TechnicalAddress <TechAdr>
Presence: [1..1]
Definition: Unique technical address to unambiguously identify a party for receiving messages from the
executing system.
TechnicalAddress <TechAdr> contains one of the following TechnicalIdentification2Choice
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   BICFI <BICFI> [1..1] IdentifierSet C2 2149
Or}   TechnicalAddress <TechAdr> [1..1] Text 2150
42.4.3.2.5.1  BICFI <BICFI>
Presence: [1..1]
Definition: Technical address of the party is defined as a financial institution business identifier code.
Impacted by: C2 "BICFI"
Datatype: "BICFIDec2014Identifier" on page 3320
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.022.001.02 PartyModificationRequestV02
Target2-Securities 2149 August 2026
```

