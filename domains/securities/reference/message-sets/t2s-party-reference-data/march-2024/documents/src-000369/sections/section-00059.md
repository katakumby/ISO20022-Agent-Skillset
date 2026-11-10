---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S PartyReferenceData"
source_ids: ["src-000369"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["6 reda.022.001.02 PartyModificationRequestV02", "6.4 Message Building Blocks", "6.4.3 Modification <Mod>", "6.4.3.2 RequestedModification <ReqdMod>", "6.4.3.2.5 TechnicalAddress <TechAdr>"]
file_pages: [70]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.022.001.02"]
---

# 6.4.3.2.5 TechnicalAddress <TechAdr>

Source: [src-000369](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_PartyReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_PartyReferenceData_2023_2024_v1.pdf`. Locator: one-based file pages 70 to 70.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 70

```text
ContactDetails <CtctDtls> contains the following elements (see "Contact14" on page 170 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   NamePrefix <NmPrfx> [0..1] CodeSet 171
   Name <Nm> [0..1] Text 171
   PhoneNumber <PhneNb> [0..1] Text 172
   MobileNumber <MobNb> [0..1] Text 172
   FaxNumber <FaxNb> [0..1] Text 172
   URLAddress <URLAdr> [0..1] Text 172
   EmailAddress <EmailAdr> [0..1] Text 172
   EmailPurpose <EmailPurp> [0..1] Text 172
   JobTitle <JobTitl> [0..1] Text 172
   Responsibility <Rspnsblty> [0..1] Text 172
   Department <Dept> [0..1] Text 173
   Other <Othr> [0..*]  173
     ChannelType <ChanlTp> [1..1] Text 173
     Identification <Id> [0..1] Text 173
   PreferredMethod <PrefrdMtd> [0..1] CodeSet 173
   ValidFrom <VldFr> [0..1] Date 174
   ValidTo <VldTo> [0..1] Date 174
6.4.3.2.5  TechnicalAddress <TechAdr>
Presence: [1..1]
Definition: Unique technical address to unambiguously identify a party for receiving messages from the
executing system.
TechnicalAddress <TechAdr> contains one of the following TechnicalIdentification2Choice
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   BICFI <BICFI> [1..1] IdentifierSet C2 70
Or}   TechnicalAddress <TechAdr> [1..1] Text 71
6.4.3.2.5.1  BICFI <BICFI>
Presence: [1..1]
Definition: Technical address of the party is defined as a financial institution business identifier code.
Impacted by: C2 "BICFI"
Datatype: "BICFIDec2014Identifier" on page 185
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
reda.022.001.02 PartyModificationRequestV02
Target2-Securities - Party Reference Data - Maintenance
2023 - 2024
70 March 2024
```

