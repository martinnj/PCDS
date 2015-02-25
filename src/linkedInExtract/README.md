De data vi trækker ud fra LinkedIn og den struktur de har efter udtrækningen.

**ProfileExtraction**
   
   *Basic profile*

   - id
   - first-name
   - last-name
   - maiden-name
   - headline
   - location
   - industry
   - summary
   - specialities
   - positions
   - picture-url
   - public-profile-url
   - formatted-name
   - phonetic-first-name
   - phonetic-last-name
   - formatted-phonetic-name
     
   *Full profile*

   - interests
   - date-of-birth

   *Lists*
   - educations as a List of Educations
   - courses as a List of Courses
   - publications as a List of Publications
   - patents as a List of Pantents
   - languages as a List of Languages
   - skills as a List of Skills
   - certifications as a List of Certifications
   - volunteer as a List of Volunteers

**Course**
   - id
   - name
   - number

**Education**
   - id
   - school-name
   - field-of-study
   - start-date
   - end-date
   - degree
   - activities
   - notes 

**Publication**
   - id
   - title
   - publisher:(name)
   - authors:(id)
   - authors:(name)
   - authors:(person)
   - date
   - url
   - summary

**Language** 
   - id
   - name
   - proficiency level

**Skill**
   - id
   - skill:(name)

**Certification**
   - id
   - name
   - authority:(name)
   - number
   - start-date
   - end-date

**Voluteer**
   - id
   - role
   - organization:(name)
   - cause:(name)
